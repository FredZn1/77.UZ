from django.urls import path
from .views import PageListView, PageDetailView, RegionWithDistrictsView

urlpatterns = [
    path('common/pages/', PageListView.as_view(), name='page-list'),
    path('common/pages/<slug:slug>/', PageDetailView.as_view(), name='page-detail'),
    path('common/regions-with-districts/', RegionWithDistrictsView.as_view(), name='region-with-districts'),
]
