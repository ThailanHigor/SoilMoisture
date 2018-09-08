from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    medida = random.randint(0,100)

    return render(request,'home.html',{"medida":medida})


def medicao(request):
    medida = random.randint(0,100)
    return HttpResponse(medida)
    