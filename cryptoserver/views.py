from django.shortcuts import render

def index(request):
    return render(request, 'cryptoserver/index.html')


def signin(request):
    return render(request, 'cryptoserver/bank_main.html')