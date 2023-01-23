from django.shortcuts import render, HttpResponse
import random

"""
첫번째 파라미터 인자는 요청과 관련된
여러가지 정보가 들어오도록 약속된 객체를 전달
"""
def index(request):
    return HttpResponse('<h1>Random</h1>' + str(random.random()))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read' + id)