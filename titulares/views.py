from django.http import JsonResponse
import json

def json_view(request):
    with open('titulares.json') as file:
        data = json.load(file)
    return JsonResponse(data)
