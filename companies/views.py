from django.views import generic

from companies.models import Company
from companies.forms import CompanyForm


class CompanyListView(generic.ListView):
    """Company list view."""
    model = Company
    sorting_options = ('name', '-name', 'created', '-created')
    paginate_by = 10

    def get_ordering(self):
        ordering = self.request.GET.get('sort')
        return ordering if ordering in self.sorting_options else self.sorting_options[0]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sort'] = self.get_ordering()
        return context


class CompanyDetailView(generic.DetailView):
    """Company detail view."""
    queryset = Company.objects.prefetch_related()


class CompanyCreateView(generic.CreateView):
    """Company create view."""
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_create.html'


class CompanyEditView(generic.UpdateView):
    """Company edit view."""
    model = Company
    form_class = CompanyForm
