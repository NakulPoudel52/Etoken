from django.shortcuts import render


def index(request):
    return render(request, 'DAMN/index.html')

def home(request):
    return render(request, 'DAMN/home.html')

def signup(request):
    return render(request, 'DAMN/Signup.html')

def contact(request):
    return render(request, 'DAMN/contact.html')


def hospital(request):
    return render(request, 'DAMN/hospitals.html')


def bank(request):
    return render(request, 'DAMN/bank.html')

def feed(request):
    return render(request, 'ALogin/ahome.html')