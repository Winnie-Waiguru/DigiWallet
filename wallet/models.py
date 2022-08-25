from curses.ascii import FS
from datetime import datetime
from email.policy import default
from inspect import signature
from pickle import TRUE
from symtable import Symbol
from django.db import models
from locale import currency


# Create your models here.
GENDER_CHOICE=(("M","Male"),("F","Female"))

class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=23, null= True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICE,default="female")
    address = models.CharField(max_length=23, null= True)
    age = models.SmallIntegerField(null= True)
    nationality = models.CharField(max_length=15,null=True)
    id_number = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    profile_picture=models.ImageField(default=False)
    signature=models.ImageField(default=False)
    employed=models.BooleanField(default=False)
    
class Currency (models.Model):
    country_of_origin=models.CharField(max_length=24,null=True)
    symbol=models.CharField(max_length=15,null=True)
    
class Wallet (models.Model):
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    balance=models.PositiveIntegerField()
    amount=models.PositiveIntegerField()
    date=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=15,null=True)
    pin=models.TextField(max_length=8,null=True)
    
class Account (models.Model):
    account_type=models.CharField(max_length=15,null=True)
    balance=models.PositiveIntegerField()
    account_name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
    
class Transaction(models.Model):
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=datetime.now)
    receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt')
    origin_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_receipt')
    destination_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination_account')    
    
class Card(models.Model):
    date_issued=models.DateTimeField(default=datetime.now)
    card_name=models.CharField(max_length=15,null=True)
    card_number=models.IntegerField()
    card_type=models.CharField(max_length=15,null=True)
    exipry_date=models.DateTimeField(default=datetime.now)
    card_status=models.CharField(max_length=15,null=True)
    security_code=models.IntegerField()
    signature=models.ImageField()
    wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    issuer=models.CharField(max_length=15,null=True) 
    
class Third_party (models.Model):
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Third_party_account')
    name=models.CharField(max_length=15,null=True)
    thirdparty_id=models.IntegerField()
    phone_number=models.IntegerField()       
    
class Notification (models.Model):
    notifications_id=models.IntegerField()
    name=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=15,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    receipt=models.ForeignKey('Third_party',on_delete=models.CASCADE,related_name='Notifications_receipt')    
    
class Receipt (models.Model):
    receipt_date=models.DateField(default=datetime.now)
    receipt_file=models.FileField()
    total_amount=models.PositiveIntegerField()
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Receipt_transaction')   
    
class Loan (models.Model):
    loan_type=models.CharField(max_length=15,null=True)
    amount=models.IntegerField()
    date_and_time=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate=models.IntegerField()
    guarantor=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarantor')
    pay_due_date=models.DateTimeField(default="")
    loan_balance=models.IntegerField()
    
class Reward (models.Model):
    GENDER_CHOICES=(("M","Male"),("F","Female"))
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
    date_and_time=models.DateTimeField(default=datetime.now)
    customer_id=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    bonus=models.IntegerField()    
        