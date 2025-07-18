from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.accounts.models import User


class AccountsTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:login")
        self.me_url = reverse("accounts:me")
        self.edit_url = reverse("accounts:edit")

        self.user_data = {
            "first_name": "Ali",
            "last_name": "Valiyev",
            "phone": "+998901234567",
            "password": "password123"
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().phone, self.user_data["phone"])

    def test_login_successful(self):
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, {
            "phone": self.user_data["phone"],
            "password": self.user_data["password"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_me_authenticated(self):
        self.client.post(self.register_url, self.user_data)
        login = self.client.post(self.login_url, {
            "phone": self.user_data["phone"],
            "password": self.user_data["password"]
        })
        access = login.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["phone"], self.user_data["phone"])

    def test_edit_profile(self):
        self.client.post(self.register_url, self.user_data)
        login = self.client.post(self.login_url, {
            "phone": self.user_data["phone"],
            "password": self.user_data["password"]
        })
        access = login.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        response = self.client.post(self.edit_url, {
            "first_name": "Ali",
            "last_name": "Karimov",
            "phone": "+998901234567"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["last_name"], "Karimov")
