from django.urls import path, include
from .views import EmployeeViewSet, EmployeeRegistrationView, EmployeeLoginView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"emp-list", EmployeeViewSet, basename="Employee List")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", EmployeeRegistrationView.as_view(), name="register"),
    path("login/", EmployeeLoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
]
