from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def main(request):
    if request.method == 'GET':
        return HttpResponse('''file processing ability page''')
    elif request.method == 'POST':
        #path = request.POST["path"]
        path_json = json.loads(request.body)
        path = path_json['path']
        return HttpResponse(path)
