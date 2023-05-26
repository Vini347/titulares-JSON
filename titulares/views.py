from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def retorno_json(request):
    data = request.body.decode('utf-8')
    print(data)
    json_data = json.loads(data)
    print(json_data)
    return HttpResponse('Done')