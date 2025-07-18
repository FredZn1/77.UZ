from rest_framework import serializers
from .models import Page, Region, District


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ("id", "title", "slug", "content", "created_at", "updated_at")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "slug": instance.slug,
            "content": instance.content,
            "created_at": instance.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": instance.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "name")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
        }


class RegionWithDistrictsSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ("id", "name", "districts")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "districts": DistrictSerializer(instance.districts.all(), many=True).data,
        }
