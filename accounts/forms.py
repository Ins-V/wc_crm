from django import forms
from django.contrib.auth import get_user_model

from common.widgets import ClearableFileWidget


UserModel = get_user_model()


class AccountSettingsForm(forms.ModelForm):
    """Account settings form."""
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'photo')
        widgets = {'photo': ClearableFileWidget}
