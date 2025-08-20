from django.urls import path
from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterView.as_view(), name="register"),
    path("accounts/seller/registration/", views.SellerRegisterView.as_view(), name="seller-register"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path("accounts/me/", views.MeView.as_view(), name="me"),
    path("accounts/edit/", views.EditProfileView.as_view(), name="edit-profile"),
    path("accounts/token/refresh/", views.TokenRefreshCustomView.as_view(), name="token-refresh"),
    path("accounts/token/verify/", views.TokenVerifyCustomView.as_view(), name="token-verify"),
]
