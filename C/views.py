from django.shortcuts import render
from django.http import *

# Create your views here.


def ricky(request):
    return HttpResponse('hi ricky')


