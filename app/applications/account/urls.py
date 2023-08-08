from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account import views

# from applications.account.custom_auth import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', views.AuthApiView.as_view()),
    path('invite_code/', views.AddAnotherUserAPIView.as_view()),
    path('user/<int:pk>/', views.UserDetailAPIView.as_view()),
]
