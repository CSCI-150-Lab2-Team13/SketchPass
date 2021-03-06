from django import forms
from mainApp.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import validate_email
from django.contrib.auth import authenticate


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


class ResendActivationLinkForm(forms.Form):
    email = forms.EmailField(label="Email", required = True, max_length=254)


class ResetPasswordForm (forms.ModelForm):
	password_reset = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)
	class Meta:
		model = User
		fields = () #custom defined above


	def clean (self):
		super(ResetPasswordForm,self).clean()
		password_reset = self.cleaned_data.get('password_reset')
		usedNums = set()
		uniqueColors = 0
		for char in password_reset:
			if int(char) > 8 or int(char) < 0:
				self.add_error(None, 'Either your email or password is incorrect!"')
				break
			usedNums.add(int(char))

		if len(usedNums) < 2:
			self.add_error(None, 'You must use 2 or more colors!')

		

	def save(self, commit = True):

		user = super(ResetPasswordForm,self).save(commit=False)	
		user.password = make_password(self.cleaned_data['password_reset'])
		if commit:
			user.save()
		return user
