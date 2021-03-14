from django import forms

from interactions.models import Interaction, Keyword
from interactions.widgets import SelectAsStarsWidget


class InteractionForm(forms.ModelForm):
    """Form for create and edit interactions."""
    class Meta:
        model = Interaction
        fields = '__all__'
        widgets = {'evaluation': SelectAsStarsWidget}


class KeywordFilterForm(forms.Form):
    """Form for filtering interactions by keywords."""
    keyword = forms.MultipleChoiceField(
        label="Фильтр по ключевым словам",
        choices=Keyword.objects.all().values_list('slug', 'word')
    )
