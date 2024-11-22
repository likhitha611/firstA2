from django.shortcuts import render
from django.http import HttpResponse
def python(request):
    return HttpResponse('python is a interpreted language')


def java(request):
    return HttpResponse('<h1> java is a software </h1>')

def sql(request):
    return HttpResponse('<h1><marquee> sql is a database</h1></marquee>')
