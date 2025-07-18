from django.urls import path
from .views import PageListView, PageDetailView, RegionWithDistrictsView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='page-list'),
    path('pages/<slug:slug>/', PageDetailView.as_view(), name='page-detail'),
    path('regions-with-districts/', RegionWithDistrictsView.as_view(), name='region-with-districts'),
]
