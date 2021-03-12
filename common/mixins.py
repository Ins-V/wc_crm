class SortingMixin:
    """Mixin for adding sorting to views based on ListView.

    When using the mixin, it is imperative to override the `sorting_options` property.
    `sorting_options` must be a list or tuple of allowed sorting methods. Everything that
    can be given to the order_by method.

    Example:
        class MyListView(SortingMixin, ListView):
            model = MyModel
            sorting_options = ('name', '-name',)
    """
    sorting_options = ['pk']

    def get_ordering(self):
        ordering = self.request.GET.get('sort')
        return ordering if ordering in self.sorting_options else self.sorting_options[0]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sort'] = self.get_ordering()
        return context
