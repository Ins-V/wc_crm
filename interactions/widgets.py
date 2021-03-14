from django.forms import widgets


class SelectAsStarsWidget(widgets.ChoiceWidget):
    """The widget for a selection field, displayed as a set of stars."""
    class Media:
        js = ('evaluation_widget.js',)

    template_name = 'interactions/widgets/select_as_stars.html'
    option_template_name = 'interactions/widgets/select_as_stars_option.html'
