from modeltranslation.translator import TranslationOptions, register
from .models import Page, Region, District, Setting


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields = ("working_hours",)
