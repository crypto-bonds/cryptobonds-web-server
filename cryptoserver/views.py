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
        except Exception as e:
            print(e)
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

def cwithdraw(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'cryptoserver/company_withdraw.html', {'company': company})

def cdeposit(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'cryptoserver/company_deposit.html', {'company': company})

def crequest(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'cryptoserver/company_request.html', {'company': company})

def bdeposit(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    return render(request, 'cryptoserver/bank_deposit.html', {'bank': bank})

def bwithdraw(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    return render(request, 'cryptoserver/bank_withdraw.html', {'bank': bank})

def baccept(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    return render(request, 'cryptoserver/bank_accept.html', {'bank': bank})

def twithdraw(request):
    return render(request, 'cryptoserver/trader_deposit.html')

def withdraw(request):
    pass

