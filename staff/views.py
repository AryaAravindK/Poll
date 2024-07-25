from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def staff(request):
    return HttpResponse('staff page')