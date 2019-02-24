from django.db import models

class Bank(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    money = models.IntegerField()
    public_key = models.CharField(max_length=500)


class Trader(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    money = models.IntegerField()


class Company(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    money = models.IntegerField()


class Bond(models.Model):
    issuer = models.ForeignKey(Company, on_delete=models.CASCADE)
    underwriter = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.IntegerField()
    denomination = models.IntegerField()
    interest_rate = models.IntegerField()
    maturity_date = models.DateTimeField()