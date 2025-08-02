from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city=request.GET.get('city','bangalore') 
    api_key='e897ba6860324469b09140d02d042dd3'
    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    print(api_url)
    api=requests.get(api_url).json()

    temperature=api['main']['temp']
    country=api['sys']['country']
    city=api['name']



    return render(request, 'index.html', {'temperature':temperature, 'country':country, 'city':city})