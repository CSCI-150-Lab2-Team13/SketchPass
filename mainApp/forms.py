from django import forms
from mainApp.models import User
from django.contrib.auth.hashers import make_password
class LoginForm(forms.Form):
	email_login = forms.EmailField(label = "Email", required = True)
	password_login = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	def clean(self):
		cleaned_data = super(LoginForm,self).clean()
		email_login = cleaned_data.get('email_login')
		password_login = cleaned_data.get('password_login')
		if (not email_login):
			raise forms.ValidationError("Email is invalid!", code='invalid-login-email')
	
class RegisterForm(forms.ModelForm):
	email_register = forms.EmailField(label = "Email", required = True)
	email_verify = forms.EmailField(label = "Verify Email", required = True)
	password_register = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	class Meta:
		model = User
		fields = () #custom defined above

	def clean(self):
		cleaned_data = super(RegisterForm,self).clean()
		email = cleaned_data.get('email_register')
		email_verify = cleaned_data.get('email_verify')
		password_register = cleaned_data.get('password_register')

		if (not email):
			raise forms.ValidationError('Invalid email', code='invalid-register-email')
	def clean_email(self):
		email = self.cleaned_data['email']
		not_unique = User.objects.filter(email__iexact=email).exists()
		if not_unique:
			self.add_error('email', "Email already registered!")

	def clean_email_verify(self):
		cleaned_data = super(RegisterForm,self).clean()
		email = cleaned_data.get('email_register')
		email_verify = self.cleaned_data['email_verify']
		if email != email_verify:
			self.add_error('email_verify','Emails must match!')


	def save(self, commit = True):   
		user = super(RegisterForm, self).save(commit = False)
   		user.email = self.cleaned_data['email_register']
   		user.password = make_password(self.cleaned_data['password_register'])
		if commit:
			user.save()
		return user


#For categories forms.ChoiceField(choices[('ques')]
