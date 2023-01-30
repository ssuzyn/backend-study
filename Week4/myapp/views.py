from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from myapp.seed_models import testData
from myapp.models import User
import json

T = testData()

def main(request):
    return HttpResponse('''SQL Processing Page''')

@csrf_exempt
def testUser(request):
    if request.method == 'POST':
        try:
            total = json.loads(request.body)['seed']
            #user = T.handleUser(total)
            user = User.objects.all()
            user_list = serializers.serialize("json", user, fields=("email", "password"))
            result = json.loads(user_list)
            return JsonResponse(result, safe=False, status=200)
        except Exception as ex:
            print('error !!', ex)
            return JsonResponse({"status" : "400"})
            
