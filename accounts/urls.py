from django.urls import path
from .views import register_view, login_view, logout_view, recovery_view, reset_password_view
from django.conf.urls import include


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('recovery/', recovery_view, name='recovery'),
    path('reset-password/<str:uidb64>/<str:token>/', reset_password_view, name='reset_password'),
]
