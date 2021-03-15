def login_exempt(view):
    """A decorator to mark the view as not requiring authentication."""
    view.login_exempt = True
    return view
