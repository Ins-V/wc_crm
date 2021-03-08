from django import forms

from companies.models import Phone, Email, Company


class CompanyForm(forms.ModelForm):
    """Form for create and edit company."""
    class Meta:
        model = Company
        fields = ('name', 'description', 'contact_person', 'address', 'phones', 'emails')


class CompanyPhoneForm(forms.ModelForm):
    """Form for create company phone."""
    class Meta:
        model = Phone
        fields = '__all__'


class CompanyEmailForm(forms.ModelForm):
    """Form for create company email."""
    class Meta:
        model = Email
        fields = '__all__'
