from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('<int:company_id>/company_withdraw/', views.cwithdraw, name='cwithdraw'),
    path('<int:company_id>/company_deposit/', views.cdeposit, name='cdeposit'),
    path('<int:company_id>/company_request/', views.crequest, name='crequest'),

    path('bank_withdraw/', views.bwithdraw, name='bwithdraw'),
    path('trader_deposit_withdraw/', views.twithdraw, name='twithdraw'),
]