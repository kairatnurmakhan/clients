from django.shortcuts import render, HttpResponse
from .models import Clients

# Create your views here.


def clients(request):
    context = {}
    # SELECT * FROM Clients
    clients_list = Clients.objects.all()
    context['clients_list'] = clients_list
    return render(request, 'clients.html', context)
    # html_page = render(request, 'clients.html', context)
    # return  html_page


def about(request):
    return render(request, 'about.html')


def products(request):
    response = HttpResponse('Legenda, Corona, Asuu')
    return response
