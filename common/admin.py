from django.contrib import admin
from .models import Page, Region, District


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
