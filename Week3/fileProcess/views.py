from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os, xmltodict, csv, yaml

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
        return JsonResponse({"status" : "ok", "body" : data})

@csrf_exempt
def csvFile(request):
    if request.method == 'GET':
        return HttpResponse('''csv file page''')
    elif request.method == 'POST':
        data = []
        path = json.loads(request.body)['path']
        file = csv.DictReader(open(path + '.csv'))

        for row in file:
            data.append(row)

        return JsonResponse({"status" : "ok", "body" : data})

@csrf_exempt
def yamlFile(request):
    if request.method == 'GET':
        return HttpResponse('''csv file page''')
    elif request.method == 'POST':
        data =[]
        path = json.loads(request.body)['path']
        file = yaml.safe_load(open(path + '.yaml'))
        return JsonResponse({"status" : "ok", "body" : file})