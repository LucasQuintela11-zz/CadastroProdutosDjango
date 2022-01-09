from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contato(request):
    return request(request, 'contato.html')

def produto(request):
    return request(request, 'produto.html')

