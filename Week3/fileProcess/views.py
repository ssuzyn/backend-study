from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os, xmltodict, csv

def main(request):
    return HttpResponse('''file processing ability page''')

@csrf_exempt
def jsonFile(request):
    print(os.getcwd())
    if request.method == 'GET':
        return HttpResponse('''JSON file page''')
    elif request.method == 'POST':
        path = json.loads(request.body)['path']
        file = open(path + '.json')
        data = json.load(file)

        return JsonResponse({"status" : "ok", "body" : data})

@csrf_exempt
def xmlFile(request):
    if request.method == 'GET':
        return HttpResponse('''xml file page''')
    elif request.method == 'POST':
        path = json.loads(request.body)['path']
        file = open(path + '.xml')
        data= xmltodict.parse(file.read())
        print(data)
        return JsonResponse({"status" : "ok", "body" : data})

@csrf_exempt
def csvFile(request):
    if request.method == 'GET':
        return HttpResponse('''csv file page''')
    elif request.method == 'POST':
        path = json.loads(request.body)['path']
        file = open(path + '.csv')
        reader = csv.DictReader(file)
        data = json.dumps(list(reader))
        print(data)
        return JsonResponse({"status" : "ok", "body" : data})