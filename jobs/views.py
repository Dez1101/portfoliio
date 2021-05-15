from django.shortcuts import render

# Create your views here.
class home(request):
    return render(request, 'home.html')