from django.shortcuts import render

def index(request):
    return render(request, 'cryptoserver/index.html')


def signin(request):
    selection = request.POST['inlineFormCustomSelect']
    if selection == '1':
        return render(request, 'cryptoserver/bank_main.html')
    elif selection == '2':
        return render(request, 'cryptoserver/company_main.html')
    else:
        return render(request, 'cryptoserver/trader_main.html')
