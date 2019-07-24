from django.shortcuts import render

click = False

def solucao(request):
    return render(request, 'solucao.html')

