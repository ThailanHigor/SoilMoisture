from django.shortcuts import render
from django.http import HttpResponse
from gpiozero import MCP3008
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


SENSORES_PESOS = [0,0]
SENSORES_PINOS = [0,3]

def home(request):
    SENSORES_PESOS[0] = MCP3008(0).value
    SENSORES_PESOS[1] = MCP3008(2).value
    return render(request,'home.html')


def medir(valor,peso):
    x = (valor * 100) / float(peso)
    return x

@csrf_exempt
def medicao (request):

    higro = MCP3008(0)
    #peso = SENSORES_PESOS[0]
    #valor_medido = medir(1 - higro.value,peso)
    #print(valor_medido)

    return HttpResponse(1-higro.value)

@csrf_exempt
def calibrar(request):
    #pega os campos do ajax
    media = request.POST.get('media')
    sensor = int(request.POST.get('sensor'))
    

    #realiza a leitura do sensor selecionado
    higro = MCP3008(sensor)
    
    #atualiza valores dos pesos
    SENSORES_PESOS[sensor] = float(media)

    #retorno do valor lido pelo sensor
    
    medida =  higro.value
    return HttpResponse(medida)
    