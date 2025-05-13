from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.useraccount_view import UserAccountView

router = DefaultRouter()

router.register(
    prefix=r'users',
    viewset=UserAccountView,
    basename='users'
)


urlpatterns = [
    path('', include(router.urls)),
]
