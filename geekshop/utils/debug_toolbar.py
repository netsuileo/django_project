from debug_toolbar.middleware import show_toolbar

def show_debug_toolbar(request):
    """
    Default function to determine whether to show the toolbar on a given page.
    """
    return show_toolbar or bool(request.GET.get('debug', False))
