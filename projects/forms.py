from django import forms

from projects.models import Project


class ProjectForm(forms.ModelForm):
    """Form for create and edit project of companies.

    The form is based on ModelForm and adds a datepicker class for date fields
    and disables autocomplete for them.
    """
    class Meta:
        model = Project
        fields = ('name', 'price', 'company', 'start_date', 'end_date', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs = {'autocomplete': 'off', 'class': 'datepicker'}
        self.fields['end_date'].widget.attrs = {'autocomplete': 'off', 'class': 'datepicker'}
