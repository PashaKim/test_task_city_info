from django.conf import settings
from django.core.management import BaseCommand

from main.models import City


def popout(str,n):
    '''https://stackoverflow.com/questions/44214799/attributeerror-str-object-has-no-attribute-pop'''
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back


class Command(BaseCommand):
    help = 'The madgicx_geo is a tool that helps users to get some insights about cities in the worldWhen the ' \
           'madgicx_geo gets a name of a city, it returns some interesting insights about it.'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)  # files
        parser.add_argument('-n', '--city_names', nargs='+', type=str)  # Kyiv, Vienna

    def get_str_city_row(self, city_info):
        return f"\n{city_info['name']}\n-------------\nCountry: ​ {city_info['country__name']}" \
               f"\nCurrency: {city_info['country__currency__code']}\n-------------"

    def get_str_invalid_city_row(self, invalid_name):
        return f"\n{invalid_name}\n-------------\n Invalid City Name\n-------------"

    def get_city_info_from_name(self, city_names_l) -> str:
        '''Take city info from database and return it in str'''

        # for harder filtring
        # query = reduce(operator.and_, (Q(name__contains=city) for city in city_names_l))

        city_table_str = ''  # output text
        cities_db_l = City.objects.filter(name__in=city_names_l).values('name', 'country__name',
                                                                        'country__currency__code')
        cities_db_names_l = [city['name'] for city in cities_db_l]  # names of existing cities
        for name in city_names_l:
            if name in cities_db_names_l:
                city_table_str += self.get_str_city_row(cities_db_l[cities_db_names_l.index(name)]) # look like "cities_db_l[1]" take index from cities_db_names_l
            else:
                city_table_str += self.get_str_invalid_city_row(invalid_name=name)

        return city_table_str

    def get_city_info_from_file(self, file_name):
        with open(f'{settings.BASE_DIR}/{file_name}', 'r') as file:
            city_names = file.readlines()  # ['Vienna\n', 'Kiev\n', 'New York']
        city_names = [name.replace('\n', '') for name in city_names]  # remove \n
        return self.get_city_info_from_name(city_names)

    def get_formated_names(self, city_names_l):
        city_names_l = [city.capitalize() for city in city_names_l]  # format name in one type
        city_names_l = (' '.join(city_names_l)).split(',') # 'Tel', 'Aviv' to 'Tel Aviv'
        city_names_l = [popout(name, 0) if name[0] == ' ' else name for name in city_names_l]  # for remove additional space
        return city_names_l

    def handle(self, *args, **options):
        if options['file']:
            print(self.get_city_info_from_file(options['file']))
        elif options['city_names']:
            print(self.get_city_info_from_name(self.get_formated_names(options['city_names'])))

        else:  # if no arg selected
            print(self.help + '\n Please enter city name separated by commas(-n <names, >) or add a file(-f <file>)' +
                  f'\n Available city names: {", ".join(City.objects.values_list("name", flat=True))}')
