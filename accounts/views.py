from django.contrib.auth import views
from django.urls import reverse, reverse_lazy


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('company:list')


class LogoutView(views.LogoutView):
    next_page = reverse_lazy('account:login')


class PasswordResetView(views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
