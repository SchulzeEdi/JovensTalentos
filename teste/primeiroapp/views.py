from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def diga_oi(request):
  # Buscar dados de base
  # Manipular dados
  # Mandar emails...
  return render(request, 'oi.html')