from django.shortcuts import render, HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse('Pasame la materia')

