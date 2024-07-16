from django.urls import path, include
from .views import UserAuth, RegisterView, LoginView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserAuth.as_view(), name='user-auth'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    path('api-token-auth/', obtain_auth_token),
]