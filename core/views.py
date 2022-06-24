from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views import View
from .models import FavoriteCity

# Функции 

def forecastAPI(city):
    # https://www.weatherapi.com/
    key = '6a0482faf2c9400db0a200652221706'
    url = f'https://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days=3&aqi=no&alerts=no'
    if (requests.get(url).status_code != 200):
        return 'error'
    else:
        return requests.get(url).json()

def is_favorite(city_name, user):
    city = FavoriteCity.objects.filter(user = user, name = city_name).count()
    return bool(city)

def change_favorite_state(city_name, user):
    if is_favorite(city_name, user):
        FavoriteCity.objects.filter(user = user, name = city_name).delete()
    else:
        FavoriteCity.objects.create(user = user, name = city_name)
    return HttpResponse('success')

def forecast(city, context, hours=12):
    result = forecastAPI(city)
    current_hour = int(result['location']['localtime'][-5:][:2])
    range_end = (13 + hours) - abs(12 - current_hour) if current_hour <= 12 else (13 + hours) + (current_hour + 11) % 12 + 1
    for i in range(current_hour + 1 , range_end):
                if i < 24:
                    hour = f'{i-12} PM' if i > 12 else f'{i} AM'
                    forecast = {
                        'hour' : hour,
                        'temp' : result['forecast']['forecastday'][0]['hour'][i]['temp_c'],
                        'icon' : result['forecast']['forecastday'][0]['hour'][i]['condition']['icon'],
                    }
                    context.append(forecast)
                else:
                    hour = f'{i-24} AM'
                    forecast = {
                        'hour' : hour,
                        'temp' : result['forecast']['forecastday'][1]['hour'][i-24]['temp_c'],
                        'icon' : result['forecast']['forecastday'][1]['hour'][i-24]['condition']['icon'],
                    }
                    context.append(forecast)

def get_favorites(user):
    context = []
    favorite_cities = [i.name for i in FavoriteCity.objects.filter(user = user)]
    for city in favorite_cities:
        append_data = {
            'name' : city,
            'forecast' : []
        }
        forecast(city, append_data['forecast'], 6)
        context.append(append_data)
    return context

# Views:

class IndexView(View):
    template_path = 'core/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            context = {'favorites' : get_favorites(request.user)}
            return render(request, self.template_path, context=context)
        else:
            return render(request, self.template_path, context={})

    def post(self, request):
        if not request.POST.get('favorite_change', False):
            city = request.POST['city']
            result = forecastAPI(city)
            if (result == 'error'): 
                return render(request, self.template_path, context={'result' : {'error' : True, 'city' : city}})
            context = {
                'result' : {
                    'error' : False,
                    'city' : result['location']['name'],
                    'country' : result['location']['country'],
                    'current' : {
                        'temperature' : result['current']['temp_c'],
                    },
                    'forecast' : {
                        'hour_forecast' : []
                    },
                }   
            }
            forecast(city, context['result']['forecast']['hour_forecast'])
            # Проверка является ли место избранным
            if request.user.is_authenticated: 
                context['result']['is_favorite'] = is_favorite(result['location']['name'], request.user)
                context['favorites'] = get_favorites(request.user)
            return render(request, self.template_path, context=context)

        elif request.POST.get('favorite_change', False):
            return change_favorite_state(request.POST['favorite_change'], request.user)
