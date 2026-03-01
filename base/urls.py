from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('send-message/', views.send_message, name='send_message'),
]

if getattr(settings, 'SIGNIN_GOOGLE', False):
    urlpatterns.append(path('accounts/', include('allauth.urls')))
else:
    urlpatterns += [
        path('login/', views.login_view, name='login'),
        path('register/', views.register_view, name='register'),
    ]
