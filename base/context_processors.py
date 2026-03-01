from django.conf import settings


def auth_context(request):
    """
    Add authentication context variables to all templates.
    Provides signin_google flag and the appropriate login URL.
    """
    signin_google = getattr(settings, 'SIGNIN_GOOGLE', False)

    if signin_google:
        auth_login_url = '/accounts/google/login/?process=login'
    else:
        from django.urls import reverse
        auth_login_url = reverse('login')

    return {
        'signin_google': signin_google,
        'auth_login_url': auth_login_url,
    }
