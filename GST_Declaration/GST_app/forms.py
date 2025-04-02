# app_name/forms.py
from django import forms
from .models import GSTDeclaration
import re

class GSTForm(forms.ModelForm):
    class Meta:
        model = GSTDeclaration
        fields = ['gst_number', 'date_of_filing', 'mobile_number', 'address', 'pan_number']
        widgets = {
            'gst_number': forms.TextInput(attrs={'placeholder': 'Enter GST Number', 'class': 'form-control'}),
            'date_of_filing': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter Address', 'class': 'form-control', 'rows': 3}),
            'pan_number': forms.TextInput(attrs={'placeholder': 'Enter PAN Number', 'class': 'form-control'}),
        }

    def clean_gst_number(self):
        """ Validate GST Number Format (15 Characters) """
        gst_number = self.cleaned_data.get('gst_number')
        if not re.match(r'^[0-9A-Z]{15}$', gst_number):
            raise forms.ValidationError("Invalid GST Number format. It should be 15 characters long.")
        return gst_number

    def clean_mobile_number(self):
        """ Validate Mobile Number (10 Digits) """
        mobile_number = self.cleaned_data.get('mobile_number')
        if not re.match(r'^\d{10}$', mobile_number):
            raise forms.ValidationError("Invalid Mobile Number. It should be 10 digits long.")
        return mobile_number

    def clean_pan_number(self):
        """ Validate PAN Number Format (5 letters, 4 digits, 1 letter) """
        pan_number = self.cleaned_data.get('pan_number')
        if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan_number):
            raise forms.ValidationError("Invalid PAN Number format. Example: ABCDE1234F")
        return pan_number
