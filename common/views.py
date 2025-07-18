from rest_framework import generics
from .models import Page, Region
from .serializers import PageSerializer, RegionWithDistrictsSerializer


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


class RegionWithDistrictsView(generics.ListAPIView):
    queryset = Region.objects.prefetch_related('districts').all()
    serializer_class = RegionWithDistrictsSerializer
