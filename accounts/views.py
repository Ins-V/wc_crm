from django.contrib.auth import views, get_user_model
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.forms import AccountSettingsForm
from common.decorators import login_exempt


UserModel = get_user_model()


@method_decorator(login_exempt, name='dispatch')
class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('company:list')


@method_decorator(login_exempt, name='dispatch')
class LogoutView(views.LogoutView):
    next_page = reverse_lazy('account:login')


@method_decorator(login_exempt, name='dispatch')
class PasswordResetView(views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


@method_decorator(login_exempt, name='dispatch')
class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


@method_decorator(login_exempt, name='dispatch')
class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


@method_decorator(login_exempt, name='dispatch')
class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'accounts/password_change_form.html'
    success_url = reverse_lazy('account:password_change_done')


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class AccountDetailView(generic.DetailView):
    """Account detail view."""
    model = UserModel
    template_name = 'accounts/account_detail.html'

    def get_object(self, queryset=None):
        return self.request.user


class AccountSettingsView(generic.UpdateView):
    """Account settings view."""
    model = UserModel
    form_class = AccountSettingsForm
    template_name = 'accounts/account_settings.html'

    def get_object(self, queryset=None):
        return self.request.user
