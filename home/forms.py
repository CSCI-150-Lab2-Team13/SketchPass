from django import forms
from mainApp.models import Website
from mainApp.models import User
from mainApp.models import UserManager

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
        	'urlNAME': "Url",
            'websiteName': "Website",
       		'desc': "Description",
       		'category': "Category",
       		'password': "Password",
            'username': "Username"
        }
