from django import forms
from mainApp.models import Users

class LoginForm(forms.Form):
	email_login = forms.EmailField(label = "Email", required = True)
	password_login = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	def clean(self):
		cleaned_data = super(LoginForm,self).clean()
		email_login = cleaned_data.get('email_login')
		password_login = cleaned_data.get('password_login')
		if (not email_login):
			raise forms.ValidationError("Email is invalid!", code='invalid-login-email')
	
class RegisterForm(forms.Form):
	email_register = forms.EmailField(label = "Email", required = True)
	email_verify = forms.EmailField(label = "Verify Email", required = True)
	password_register = forms.CharField(max_length = 100, widget = forms.HiddenInput(), required = True)

	def clean(self):
		cleaned_data = super(RegisterForm,self).clean()
		email = cleaned_data.get('email')
		email_verify = cleaned_data.get('email_verify')
		password_register = cleaned_data.get('password_register')

		if email != email_verify:
			raise forms.ValidationError('Emails must match!', code='emails-dont-match')

		if (not email):
			raise forms.ValidationError('Invalid email', code='invalid-register-email')


	def clean_email(self):
		email = self.cleaned_data['email']
		not_unique = Users.objects.filter(email__iexact=email).exists()
		if not_unique:
			  self.add_error('email', "Email already exists!")


#For categories forms.ChoiceField(choices[('ques')]
