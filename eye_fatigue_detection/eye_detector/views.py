from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os

def index(request):
    return render(request, 'eye_detector/index.html')

def run_code(request):
    try:
        # Executar o código de detecção de fadiga ocular em segundo plano
        subprocess.Popen(['C:/Users/mmnal/Documents/Trabalho_Python/env/Scripts/python.exe', 'C:/Users/mmnal/Documents/Trabalho_Python/eye_fatigue_detection/eye_detector/main/detector_fadiga.py'])
        return HttpResponse("Câmera Ligando...")
    except Exception as e:
        return HttpResponse(f"Erro durante a execução:\n{str(e)}")