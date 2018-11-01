from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label = "email-login", required = True)
	password = forms.CharField(max_length = 100, required = True)

class RegisterForm(forms.Form):
	email = forms.EmailField(label = "email-register", required = True)
	email_verify = forms.EmailField(label = "email-register-verify", required = True)
	password = forms.CharField(max_length = 100, required = True)


#For categories forms.ChoiceField(choices[('ques')]
