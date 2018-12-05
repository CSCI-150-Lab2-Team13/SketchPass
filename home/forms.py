from django import forms
from mainApp.models import Website
from mainApp.models import User
from. validator import email_used_validator

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = (
                'urlNAME',
                'websiteName',
                'username',
                'desc',
                'category',
                'password' )

        labels = {
        	"urlNAME": "Url",
            'websiteName': "Website",
       		'desc': "Description",
       		'category': "Category",
       		'password': "Password",
            'username': "Username"
        }

class EmailChangeForm(forms.Form):

    new_email = forms.EmailField(label='New email address', validators=[email_used_validator])
