from django.http import (
    HttpResponse,
    JsonResponse
)

# Utils
from datetime import datetime

def hello_world(request):
    
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"La hora actual es {str(now)}")


def sorted_json(request):
    
    numbers = request.GET['numbers'].split(',')
    numbers = [int(number) for number in numbers]
    sorted_numbers = sorted(numbers)

    return JsonResponse({ 'numbers': sorted_numbers })

def user(request, name, age):

    if age < 18:
        message = f"Lo sentimos {name}, no tienes edad para ver esta página 👀"

    else:
        message = f"Bienvenido señor {name} 🧐"

    return HttpResponse(message)