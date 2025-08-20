from django.contrib import admin
from .models import Category, Address, Ad, AdImage, FavouriteProduct, MySearch, PopularSearchTerm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "icon")
    search_fields = ("name",)
    list_filter = ("parent",)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lat", "long")
    search_fields = ("name",)


class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 1


class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "seller", "status", "price", "view_count", "published_at")
    list_filter = ("status", "category", "published_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AdImageInline]


class FavouriteProductAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "device_id", "product", "created_at")
    search_fields = ("user__username", "device_id", "product__name")
    list_filter = ("created_at",)


class MySearchAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "category", "search_query", "price_min", "price_max", "region_id", "created_at")
    search_fields = ("search_query", "user__username")
    list_filter = ("created_at", "category")


class PopularSearchTermAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "search_count", "updated_at")
    search_fields = ("name",)
    list_filter = ("category", "updated_at")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(FavouriteProduct, FavouriteProductAdmin)
admin.site.register(MySearch, MySearchAdmin)
admin.site.register(PopularSearchTerm, PopularSearchTermAdmin)
