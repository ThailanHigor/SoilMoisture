from django.shortcuts import render
from django.http import HttpResponse
from gpiozero import MCP3008
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


SENSORES_PESOS = [0.51,0.51],0.51,0.51]
SENSORES_PINOS = [0,1,2,3]

def home(request):
    #SENSORES_PESOS[0] = MCP3008(0).value
    #SENSORES_PESOS[1] = MCP3008(2).value
    return render(request,'home.html')


def medir(valor,peso):
    x = (valor * 100) / float(peso)
    return x

@csrf_exempt
def medicao (request):
    sensor = int(request.POST.get('sensor'))
    peso = SENSORES_PESOS[sensor]
    pino = SENSORES_PINOS[sensor]
    
    higro = MCP3008(pino)
    #peso = SENSORES_PESOS[0]
    valor_medido = medir(1 - higro.value,peso)
    #print(valor_medido)
    #valor = random.randint(0,100)
    #teste = higro.value
    print('sensor: ',sensor, 'valor: ',valor_medido, 'peso: ',peso)
    return HttpResponse(valor_medido)

@csrf_exempt
def calibrar(request):
    #pega os campos do ajax
    start = request.POST.get('start')
    sensor = int(request.POST.get('sensor'))
    #limpando o valor do peso
    if start == 0:
        SENSORES_PESOS[sensor] = 0      
   
    #realiza a leitura do sensor selecionado
    higro = MCP3008(sensor)
    valor_medido = higro.value
    #atualiza valores dos pesos
    SENSORES_PESOS[sensor] = float(valor_medido)
    print(SENSORES_PESOS)
    return HttpResponse(valor_medido)
    
@csrf_exempt
def calculaPeso(request):
    #pega os campos do ajax
    divisor = int(request.POST.get('divisor'))
    sensor = int(request.POST.get('sensor'))

    #atualiza peso do sensor
    SENSORES_PESOS[sensor] = SENSORES_PESOS[sensor] / divisor
    
    print(SENSORES_PESOS)
    return HttpResponse("sucesso")
    