from django.db import models

from .validators import validate_decimals_3


class Currency(models.Model):
    name = models.CharField(max_length=255)  # Hryvni
    code = models.CharField(max_length=3, unique=True)  # UAH
    symbol = models.CharField(max_length=5, blank=True)  # ₴
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Currencies'
        verbose_name = 'Currency'


class Country(models.Model):
    name = models.CharField(max_length=512)  # ex: Ukraine
    iso2_code = models.CharField(max_length=2, unique=True)  # ex: UA
    iso3_code = models.CharField(max_length=3, unique=True)  # ex: UKR
    phone_code = models.CharField(max_length=20, blank=True)  # ex: 380 or 1-787, 1-939 for Puerto Rico
    population = models.CharField(max_length=15, blank=True)  # ex: 45 415 596
    area_km2 = models.CharField(max_length=15, blank=True)  # ex: 603 700

    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='countries')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Countries'
        verbose_name = 'Country'


class City(models.Model):
    name = models.CharField(max_length=512)  # ex: Kyiv
    time_zone_utc = models.CharField(max_length=25, blank=True)  # ex: UTC+2(EET), UTC+3(EEST)
    density_by_km2 = models.FloatField(validators=[validate_decimals_3], blank=True)  # ex: 3.299

    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='cities')  # ex: id 1 - Ukraine

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Cities'
        verbose_name = 'City'

