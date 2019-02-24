from django.shortcuts import render
from .models import Bank, Trader, Company

def index(request):
    return render(request, 'cryptoserver/index.html')

def signin(request):
    username = request.POST['InputName']
    selection = request.POST['inlineFormCustomSelect']

    if selection == '1':
        bank = Bank.objects.filter(username=username)
        if bank.exists():
            return render(request, 'cryptoserver/bank_main.html', {'bank': bank})
        else:
            return render(request, 'cryptoserver/Error_404.html')

    elif selection == '2':
        company = Company.objects.filter(username=username)
        if company.exists():
            return render(request, 'cryptoserver/company_main.html',  {'company': company})
        else:
            return render(request, 'cryptoserver/Error_404.html')
    else:
        trader = Trader.objects.filter(username=username)
        if trader.exists():
            return render(request, 'cryptoserver/trader_main.html', {'trader': trader})
        else:
            return render(request, 'cryptoserver/Error_404.html')

