from django.urls import path
from .views import (
    RegisterView,
    SellerRegisterView,
    LoginView,
    MeView,
    EditProfileView,
    TokenRefreshCustomView,
    TokenVerifyCustomView,
)

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("register/seller/", SellerRegisterView.as_view(), name="seller-register"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", MeView.as_view(), name="me"),
    path("me/edit/", EditProfileView.as_view(), name="edit-profile"),
    path("token/refresh/", TokenRefreshCustomView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyCustomView.as_view(), name="token-verify"),
]
