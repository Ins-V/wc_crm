from django.shortcuts import get_object_or_404
from django.views import generic

from interactions.models import Interaction
from interactions.forms import InteractionForm, KeywordFilterForm
from companies.models import Company
from projects.models import Project


class InteractionListView(generic.ListView):
    """Interaction list view."""
    queryset = Interaction.objects.select_related().all()
    ordering = ['created']
    paginate_by = 10
    company = None
    project = None

    def get_queryset(self):
        """Filters the QuerySet by keyword, company or project if an appropriate get parameter was passed.
        Otherwise, it returns an unfiltered QuerySet. If the company or project for the filter
        does not exist, then a 404 error will be returned.
        """
        qs = super().get_queryset()
        url_params = self.request.GET

        if url_params.getlist('keyword'):
            qs = qs.filter(keywords__slug__in=url_params.getlist('keyword'))

        if url_params.get('company'):
            self.company = get_object_or_404(Company, pk=url_params.get('company'))
            return qs.filter(company=self.company)
        elif url_params.get('project'):
            self.project = get_object_or_404(Project, pk=url_params.get('project'))
            return qs.filter(project=self.project)
        else:
            return qs

    def get_context_data(self, **kwargs):
        """Adds a QuerySet of a company or project to the context if a filter is used.
        And adds keyword filter form.
        """
        context = super().get_context_data(**kwargs)
        context['company'] = self.company
        context['project'] = self.project
        context['keyword_filter_form'] = KeywordFilterForm()
        return context


class InteractionDetailView(generic.DetailView):
    """Interaction detail view."""
    model = Interaction


class InteractionEditView(generic.UpdateView):
    """Interaction edit view."""
    model = Interaction
    form_class = InteractionForm


class InteractionCreateView(generic.CreateView):
    """Interaction create view."""
    model = Interaction
    form_class = InteractionForm
    template_name = 'interactions/interaction_create.html'


class AccountInteractionListView(generic.ListView):
    """List of interactions added by the current user."""
    model = Interaction
    ordering = ['created']
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(manager=self.request.user)
