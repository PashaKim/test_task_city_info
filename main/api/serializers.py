from rest_framework import serializers

from main.models import Currency, Country, City


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'code', 'symbol')


class CountrySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Country
        fields = ('id', 'name', 'currency', 'iso2_code', 'iso3_code', 'phone_code', 'population', 'area_km2',)


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'time_zone_utc', 'density_by_km2', )
