from django.contrib import admin
from .models import Currency, Country, City


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'symbol', 'updated_at', 'created_at')
    fields = ('name', 'code', 'symbol', 'updated_at', 'created_at')
    readonly_fields = ('updated_at', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('updated_at', 'created_at')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'currency', 'iso2_code', 'iso3_code', 'phone_code', 'population', 'area_km2',
                    'updated_at', 'created_at')
    fields = ('name', 'currency', 'iso2_code', 'iso3_code', 'phone_code', 'population', 'area_km2', 'updated_at',
              'created_at')
    readonly_fields = ('updated_at', 'created_at')
    search_fields = ('name', 'iso2_code', 'iso3_code',)
    list_filter = ('currency', 'updated_at', 'created_at')
    raw_id_fields = ('currency', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'time_zone_utc', 'density_by_km2', 'updated_at', 'created_at')
    fields = ('name', 'country', 'time_zone_utc', 'density_by_km2', 'updated_at', 'created_at')
    readonly_fields = ('updated_at', 'created_at')
    search_fields = ('name', )
    list_filter = ('country', 'updated_at', 'created_at')
    raw_id_fields = ('country',)

