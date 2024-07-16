from django.urls import path, include
from .views import UserAuth
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserAuth.as_view(), name='user-auth'),
    path('api-token-auth/', obtain_auth_token),
]