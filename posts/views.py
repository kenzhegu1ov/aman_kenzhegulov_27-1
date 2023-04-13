from django.shortcuts import render, HttpResponse
import datetime


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        return HttpResponse(now)


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
