from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from mainApp.models import User
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(forms.Form):
	email_login = forms.EmailField(label = "Email", required = True)
	password_login = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	def clean(self):
		cleaned_data = super(LoginForm,self).clean()
		email_login = cleaned_data.get('email_login')
		password_login = cleaned_data.get('password_login')
		if (not email_login):
			raise forms.ValidationError("Email is invalid!", code='invalid-login-email')

		user = authenticate(email = email_login, password = password_login)

		if user is None:
			raise forms.ValidationError("Either your email or password is incorrect!", code='invalid-login-auth')


class RegisterForm(forms.ModelForm):
	email_register = forms.EmailField(label = "Email", required = True)
	email_verify = forms.EmailField(label = "Verify Email", required = True)
	password_register = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	class Meta:
		model = User
		fields = () #custom defined above

	def clean(self):
		super(RegisterForm,self).clean()
		email = self.cleaned_data.get('email_register')
		email_verify = self.cleaned_data.get('email_verify')
		password_register = self.cleaned_data.get('password_register')

		validate_email(email)

		not_unique = User.objects.filter(email__iexact=email).exists()
		if not_unique:
			self.add_error('email_register', "Email already registered!")

		if email != email_verify:
			self.add_error('email_verify','Emails must match!')

		usedNums = set()
		uniqueColors = 0

		for char in password_register:
			if int(char) > 8 or int(char) < 0:
				self.add_error(None, 'Either your email or password is incorrect!"')
				break
			usedNums.add(int(char))

		if len(usedNums) < 2:
			self.add_error(None, 'You must use 2 or more colors!')




	def save(self, commit = True):
		user = super(RegisterForm, self).save(commit = False)
   		user.email = self.cleaned_data.get('email_register')
   		user.password = make_password(self.cleaned_data['password_register'])
		if commit:
			user.save()
		return user

#For categories forms.ChoiceField(choices[('ques')]

class ResetPasswordForm(forms.Form):
	user_email = forms.EmailField(label = "Email", required = True)
	def send_mail(self,subject_template_name, email_template_name, context , to_email , html_email_template_name=None):
		subject = loader.render_to_string(subject_template_name,context)
		subject = ''.join(subject.spitlines())
		body = loader.render_to_string(email_template_name,context)

		email_message = EmailMultiAlternatives(subject,body,from_mail,[to_email])
		if html_email_template_name is not None:
			html_email = loader.render_to_string(html_email_template_name,context)
			email_message.attach_alternative(html_email,'text/html')
		email_message.send()
	def get_user(self,email):
			"""Given an email, return matching user(s) who should receive a reset.  """
			active_users = get_user_model()._default_manager.filter(
				email__iexact=user_email, is_active=True)
			return (u for u in active_users if u.has_usable())

	def save(self, domain_overide= None,
	 		subject_template_name='registration/password_reset_subject.txt',
			email_template_name='registration/password_reset_email.html', use_https=False, token_generator=default_token_generator,
		 	from_email=None, request=None, html_email_template_name=None):
		email = self.cleaned_data["user_email"]
		for user in self.get_users(email):
			if not domain_overide:
				current_site = get_current_site(request)
				site_name = current_site.name
				domain = current_site.domain
			else:
				site_name = domain = domain_overide
			context = {
			'email': user.email,
			'domain' : domain,
			'site_name' : site_name,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			'user': user,
			'token': token_generator.make_token(user),
            'protocol': 'https' if use_https else 'http',
			}

			self.send_mail(subject_template_name,email_template_name,context,from_email, user.email,
			 				html_email_template_name = html_email_template_name)
