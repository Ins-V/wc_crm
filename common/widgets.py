from django import forms


class ClearableFileWidget(forms.widgets.ClearableFileInput):
    """Custom widget ClearableFileInput.

    It just replaces the template that matches the materialize css.
    """
    template_name = 'common/widgets/clearable_file_input.html'
