from django import forms

from interactions.models import Interaction
from interactions.widgets import SelectAsStarsWidget


class InteractionForm(forms.ModelForm):
    """Form for create and edit interactions."""
    class Meta:
        model = Interaction
        fields = '__all__'
        widgets = {'evaluation': SelectAsStarsWidget}
