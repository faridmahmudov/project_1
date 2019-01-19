from django.shortcuts import render

def do_home(request):
    return render(request, 'home/home.html')