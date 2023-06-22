from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.ProductViewSet, basename='product')

urlpatterns = [
    path('my/', views.MyProductAPIView.as_view()),
]

urlpatterns += router.urls
