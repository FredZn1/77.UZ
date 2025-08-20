from modeltranslation.translator import TranslationOptions, register
from .models import Category, Address, Ad, PopularSearchTerm


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Ad)
class AdTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(PopularSearchTerm)
class PopularSearchTermTranslationOptions(TranslationOptions):
    fields = ("name",)
