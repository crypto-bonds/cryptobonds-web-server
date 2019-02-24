from django.shortcuts import render
from .models import Bank, Trader, Company

def index(request):
    return render(request, 'cryptoserver/index.html')


def signin(request):
    username = request.POST['InputName']
    selection = request.POST['inlineFormCustomSelect']

    if selection == '1':
        try:
            bank = Bank.objects.get(username=username)
            return render(request, 'cryptoserver/bank_main.html', {'bank': bank})
        except:
            return render(request, 'cryptoserver/Error_404.html')

    elif selection == '2':
        try:
            company = Company.objects.get(username=username)
            return render(request, 'cryptoserver/company_main.html',  {'company': company})
        except:
            return render(request, 'cryptoserver/Error_404.html')
    else:
        try:
            trader = Trader.objects.get(username=username)
            return render(request, 'cryptoserver/trader_main.html', {'trader': trader})
        except:
            return render(request, 'cryptoserver/Error_404.html')


def withdraw(request):
    pass

