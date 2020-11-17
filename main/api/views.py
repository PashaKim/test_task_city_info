from rest_framework import viewsets, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from main.api.serializers import CurrencySerializer, CountrySerializer, CitySerializer
from main.models import Currency, Country, City


class CurrencyViewSet(viewsets.ModelViewSet):
    '''List of currencies'''
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)


class CountryViewSet(viewsets.ModelViewSet):
    '''List of countries'''
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)


class CityViewSet(viewsets.ModelViewSet):
    '''List of cities'''
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    http_method_names = ('get',)


class CityInfoAPIView(views.APIView):
    permission_classes = (AllowAny,)

    def get_error_data(self, text):
        return {
            'error': text,  # error text
            'cities_list': City.objects.values('name', 'country__name')
        }

    def get(self, request,  format=None):
        ''' Api for city information by name in param :return json '''

        city_name = request.GET.get('name', '')

        if not city_name:
            return Response(self.get_error_data(text='select city name parameter - /?name=<str>'),
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                obj = City.objects.get(name=city_name)
            except City.DoesNotExist:
                return Response(self.get_error_data(text='city name does not exist'), status=status.HTTP_404_NOT_FOUND)

            serializer = CitySerializer(obj)  # Get city json with country and currency
            return Response(serializer.data, status=status.HTTP_200_OK)
