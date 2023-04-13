from django.shortcuts import render, HttpResponse, redirect
import datetime


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        return HttpResponse(str(now))


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
