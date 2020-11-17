from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from .views import CurrencyViewSet, CountryViewSet, CityViewSet

router = routers.DefaultRouter()

router.register('currency', CurrencyViewSet, base_name='currency')
router.register('country', CountryViewSet, base_name='country')
router.register('city', CityViewSet, base_name='city')

schema_view = get_schema_view()

urlpatterns = [
    path('', include(router.urls)),
    path('', schema_view),
]