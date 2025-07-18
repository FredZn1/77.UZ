from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("seller/registration/", views.SellerRegisterView.as_view(), name="seller-register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("me/", views.MeView.as_view(), name="me"),
    path("edit/", views.EditProfileView.as_view(), name="edit-profile"),
    path("token/refresh/", views.TokenRefreshCustomView.as_view(), name="token-refresh"),
    path("token/verify/", views.TokenVerifyCustomView.as_view(), name="token-verify"),
]
