from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import generic

from companies.models import Company, Phone, Email
from companies.forms import CompanyForm, CompanyPhoneForm, CompanyEmailForm
from common.mixins import SortingMixin


class CompanyListView(SortingMixin, generic.ListView):
    """Company list view."""
    model = Company
    sorting_options = ('name', '-name', 'created', '-created')
    paginate_by = 10


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


class CompanyContactsView(generic.TemplateView):
    """Company contacts view."""
    template_name = 'companies/company_contacts.html'


class CompanyPhoneListView(generic.ListView):
    """Company phone list view."""
    model = Phone
    ordering = ['pk']
    paginate_by = 10


class CompanyPhoneCreateView(generic.CreateView):
    """View for adding a new company phone."""
    model = Phone
    form_class = CompanyPhoneForm
    success_url = reverse_lazy('company:phone_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Добавить новый номер телефона"
        return context


class CompanyPhoneEditView(generic.UpdateView):
    """View for updating company phone."""
    model = Phone
    form_class = CompanyPhoneForm

    def get_success_url(self):
        return reverse('company:phone_edit', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Изменить номер телефона"
        return context

    def form_valid(self, form):
        messages.info(self.request, "Номер успешно обновлён.")
        return super().form_valid(form)


class CompanyPhoneDeleteView(generic.DeleteView):
    """View for delete company phone."""
    model = Phone
    success_url = reverse_lazy('company:phone_list')


class CompanyEmailListView(generic.ListView):
    """Company email list view."""
    model = Email
    ordering = ['pk']
    paginate_by = 10


class CompanyEmailCreateView(generic.CreateView):
    """View for adding a new company email."""
    model = Email
    form_class = CompanyEmailForm
    success_url = reverse_lazy('company:email_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Добавить новый адрес электронной почты"
        return context


class CompanyEmailEditView(generic.UpdateView):
    """View for updating company email."""
    model = Email
    form_class = CompanyEmailForm

    def get_success_url(self):
        return reverse('company:email_edit', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Изменить адрес электронной почты"
        return context

    def form_valid(self, form):
        messages.info(self.request, "Адрес электронной почты успешно обновлён.")
        return super().form_valid(form)


class CompanyEmailDeleteView(generic.DeleteView):
    """View for delete company email."""
    model = Email
    success_url = reverse_lazy('company:email_list')
