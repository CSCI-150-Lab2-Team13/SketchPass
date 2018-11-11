from django import forms
from mainApp.models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = (
                'urlNAME',
                'websiteName',
                'desc',
                'category',
                'password' )

        labels = {
        	"urlNAME": "Url",
            'websiteName': "Website",
       		'desc': "Description",
       		'category': "Category",
       		'password': "Password"
        }