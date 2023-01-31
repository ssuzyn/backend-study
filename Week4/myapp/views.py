from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from myapp.db.seed_models import testData
from myapp.db.models import User
import json

T = testData()

def main(request):
    return HttpResponse('''SQL Processing Page''')

@csrf_exempt
def testUser(request):
    if request.method == 'POST':
        try:
            total = json.loads(request.body)['seed']
            user = T.handleUser(total)
            #user = User.objects.all()
            user_list = serializers.serialize("json", user)
            result = json.loads(user_list)
            return JsonResponse(result, safe=False, status=200)

        except Exception as ex:
            print('error !!', ex)
            return JsonResponse({"status" : "400"})
            
@csrf_exempt
def testPost(request):
    if request.method == 'POST':
        try:
            total = json.loads(request.body)['seed']
            post = T.handlePost(total)
            post_list = serializers.serialize("json", post)
            result = json.loads(post_list)
            return JsonResponse(result, safe=False, status=200)

        except Exception as ex:
            print('error !!', ex)
            return JsonResponse({"status" : "400"})