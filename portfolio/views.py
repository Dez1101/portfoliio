from django.shortcuts import render

def home(request):
    name = 'Dez'
    return render(request, 'home.html', {'name':name})