from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(
    prefix=r'users',
    viewset=views.UserAccountView,
    basename='users'
)

urlpatterns = [
    path('', include(router.urls)),
]
