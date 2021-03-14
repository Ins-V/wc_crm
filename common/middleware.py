from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class LoginRequiredMiddleware:
    """Middleware for all views requires a login.

    To exclude a view from checking, the login_exempt decorator is used.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            return None

        if getattr(view_func, 'login_exempt', False):
            return None

        if reverse_lazy('admin:login') == request.path:
            return None

        login_url = reverse_lazy('account:login')
        return login_required(view_func, login_url=login_url)(request, *view_args, **view_kwargs)
