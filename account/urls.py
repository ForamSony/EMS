from django.urls import path, include
from .views import (EmployeeViewSet, EmployeeRegistrationView, EmployeeLoginView, TokenRefreshView, LogoutView,
                    EmployeeProfileView, EmployeeChangePasswordView, SendPasswordResetEmailView,
                    UserPasswordResetView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"emp-list", EmployeeViewSet, basename="Employee List")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", EmployeeRegistrationView.as_view(), name="register"),
    path("login/", EmployeeLoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", EmployeeProfileView.as_view(), name="profile"),
    path("changepassword/", EmployeeChangePasswordView.as_view(), name="changepassword"),
    path('send-password-reset-email/', SendPasswordResetEmailView.as_view(), name="SendPasswordResetEmail"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name="reset_password"),
]
