from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    # login token
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token_login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token_logout'),
    # change password
    # reset password
    # login jwt
    path('token/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('token/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('token/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]