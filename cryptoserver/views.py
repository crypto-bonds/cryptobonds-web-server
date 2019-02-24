from django.shortcuts import render

def index(request):
    return render(request, 'cryptoserver/index.html')


def signin(request):
    print(request.method)
    return render(request, 'cryptoserver/bank_main.html')