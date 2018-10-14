from django.shortcuts import render
from django.http import HttpResponse
from gpiozero import MPC3008
import random
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


SENSORES_PESOS = [0,0,0,0,0]
SENSORES_PINOS = [2,3,4,5,7]

def home(request):
    return render(request,'home.html')


def medir(valor,peso):
    x = (valor * 100) / float(peso)
    return x

def medicao (request):
    valor_medido = [0,0,0,0,0]
    for i in SENSORES_PINOS:
        higro = MCP3008(i)
        peso = SENSORES_PESOS[i]
        valor_medido[i] = medir(1 - higro.value,peso)

    payload = {'g1':valor_medido[0],'g2': valor_medido[1], 'g3':valor_medido[2],'g4':valor_medido[3],'g5':valor_medido[4]}
    return JsonResponse(payload)

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
    