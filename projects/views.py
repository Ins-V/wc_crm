from django.urls import reverse_lazy
from django.views import generic

from projects.models import Project
from projects.forms import ProjectForm
from common.mixins import SortingMixin


class ProjectListView(SortingMixin, generic.ListView):
    """Project list view."""
    queryset = Project.objects.select_related()
    sorting_options = ('name', '-name', 'start_date', '-start_date', 'end_date', '-end_date')
    paginate_by = 10


class ProjectDetailView(generic.DetailView):
    """Project detail view."""
    queryset = Project.objects.select_related()


class ProjectCreateView(generic.CreateView):
    """Project create view."""
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'


class ProjectEditView(generic.UpdateView):
    """Project edit view."""
    model = Project
    form_class = ProjectForm


class ProjectDeleteView(generic.DeleteView):
    """Project delete view."""
    model = Project
    success_url = reverse_lazy('project:list')
