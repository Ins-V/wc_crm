from django.contrib.auth.decorators import login_required


class LoginRequiredMiddleware:
    """Middleware for all views requires a login.

    To exclude a view from checking, the login_exempt decorator is used.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated or getattr(view_func, 'login_exempt', False):
            return None

        return login_required(view_func)(request, *view_args, **view_kwargs)
