from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.api.serializers import CurrencySerializer, CountrySerializer, CitySerializer
from main.models import Currency, Country, City


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)
