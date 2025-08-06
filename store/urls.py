from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'my-ads', MyAdViewSet, basename='my-ads')
router.register(r'favourite-product', FavouriteProductViewSet, basename='favourite-product')
router.register(r'my-search', MySearchViewSet, basename='my-search')

urlpatterns = [
    path('', include(router.urls)),

    path('store/categories-with-childs/', CategoryWithChildrenView.as_view(), name='categories-with-childs'),
    path('store/sub-category/', CategoryViewSet.as_view({'get': 'list'}), name='sub-category'),

    path('store/list/ads/', AdViewSet.as_view({'get': 'list'}), name='ads-list'),

    path('my-favourite-product/', FavouriteProductViewSet.as_view({'get': 'list'}), name='my-favourite-product'),
    path('my-favourite-product-by-id/', FavouriteProductViewSet.as_view({'get': 'list'}),
         name='my-favourite-product-by-id'),
    path('favourite-product-by-id/<int:id>/delete/', FavouriteProductViewSet.as_view({'delete': 'destroy'}),
         name='favourite-product-by-id-delete'),
    path('favourite-product/<int:id>/delete/', FavouriteProductViewSet.as_view({'delete': 'destroy'}),
         name='favourite-product-delete'),

    path('store/my-search/list/', MySearchViewSet.as_view({'get': 'list'}), name='my-search-list'),
    path('store/my-search/<int:id>/delete/', MySearchViewSet.as_view({'delete': 'destroy'}), name='my-search-delete'),

    path('store/search/populars/', PopularSearchTermView.as_view(), name='search-populars'),
    path('store/search/count-increase/<int:id>/', SearchCountIncreaseView.as_view(), name='search-count-increase'),
    path('store/search/complete/', SearchCompleteView.as_view(), name='search-complete'),
    path('store/search/category-product/', SearchCompleteView.as_view(), name='search-category-product'),

    path('store/product-download/<slug:slug>/', ProductDownloadView.as_view(), name='product-download'),
    path('store/product-image-create/', ProductImageCreateView.as_view(), name='product-image-create'),
]