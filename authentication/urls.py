from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('register/', views.register),
    path('user-profile/', views.user_profile),
    path('', include(router.urls)),
]
