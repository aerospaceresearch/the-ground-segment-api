from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path(r'login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path(r'logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
]
