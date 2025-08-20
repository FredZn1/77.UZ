from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from .validators import validate_phone_number


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[validate_phone_number])
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "password")

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Bu telefon raqam allaqachon ro‘yxatdan o‘tgan.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "phone": instance.phone,
            "role": instance.role,
        }


class SellerRegisterSerializer(RegisterSerializer):
    def create(self, validated_data):
        validated_data["role"] = User.Role.SELLER
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["phone"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Telefon raqam yoki parol noto‘g‘ri.")
        data["user"] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "role")


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone")

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
