from django.views import generic

from companies.models import Company


class CompanyListView(generic.ListView):
    """Company list view."""
    queryset = Company.objects.prefetch_related()


class CompanyDetailView(generic.DetailView):
    """Company detail view."""
    queryset = Company.objects.prefetch_related()
