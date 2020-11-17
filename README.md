# City Info
The city_info is a tool that helps users to get some insights about cities in the world.
When the city_info gets a name of a city, it returns some interesting insights about it.

## Installation
Python 3.6, Django 2

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install -r requirements.txt
```

Create sqlite database.
```bash
python manage.py migrate
```

Create a superuser to access to admin panel by this url - http://localhost:8000/admin/
```bash
python manage.py createsuperuser
```

## Fixtures
Add data to created database
```bash
python manage.py loaddata fixtures/currency.json fixtures/country.json fixtures/city.json
```

## Api
main api schema - http://localhost:8000/api/
The endpoint provides currency, country, city json lists
```bash
{
    "currency": "http://localhost:8000/api/currency/",
    "country": "http://localhost:8000/api/country/",
    "city": "http://localhost:8000/api/city/"
}
```

curl

```bash
	curl "http://localhost:8000/api/"
```


currency list - http://localhost:8000/api/currency/

```bash
[
    {
        "id": 2,
        "name": "Euro",
        "code": "EUR",
        "symbol": "€"
    }
]
```

curl

```bash
	curl "http://localhost:8000/api/currency/"
```

country list - http://localhost:8000/api/country/

```bash
[
    {
        "id": 2,
        "name": "Austria",
        "currency": {
            "id": 2,
            "name": "Euro",
            "code": "EUR",
            "symbol": "€"
        },
        "iso2_code": "AT",
        "iso3_code": "AUT",
        "phone_code": "43",
        "population": "8 205 000",
        "area_km2": "83 858"
    }
]
```

curl

```bash
	curl "http://localhost:8000/api/country/"
```

city list - http://localhost:8000/api/city/

```bash
[
    {
        "id": 2,
        "name": "Vienna",
        "country": {
            "id": 2,
            "name": "Austria",
            "currency": {
                "id": 2,
                "name": "Euro",
                "code": "EUR",
                "symbol": "€"
            },
            "iso2_code": "AT",
            "iso3_code": "AUT",
            "phone_code": "43",
            "population": "8 205 000",
            "area_km2": "83 858"
        },
        "time_zone_utc": "UTC+1 (CET) UTC+2 (CEST)",
        "density_by_km2": 4.326
    }
]
```

curl

```bash
	curl "http://localhost:8000/api/city/"
```

city information(json) with name param - http://localhost:8000/api/city_info/?name=<city_name:str>

```bash
    {
        "id": 2,
        "name": "Vienna",
        "country": {
            "id": 2,
            "name": "Austria",
            "currency": {
                "id": 2,
                "name": "Euro",
                "code": "EUR",
                "symbol": "€"
            },
            "iso2_code": "AT",
            "iso3_code": "AUT",
            "phone_code": "43",
            "population": "8 205 000",
            "area_km2": "83 858"
        },
        "time_zone_utc": "UTC+1 (CET) UTC+2 (CEST)",
        "density_by_km2": 4.326
    }
```

curl

```bash
	curl "http://localhost:8000/api/city_info/?name=Vienna"
```

## License
[MIT](https://choosealicense.com/licenses/mit/)