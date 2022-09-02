from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Account, Card, Customer, Currency, Loan, Receipt, Reward, Third_party, Transaction, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        
class CurrencyChoiceForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__" 
       
class RegisterWalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"        
               
class RegisterAccountForm(forms.ModelForm):  
    class Meta:
        model = Account
        fields = "__all__"             
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"     
        
class RegisterCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"   
        
class RegisterThirdparty(forms.ModelForm):
    class Meta:
        model = Third_party
        fields ="__all__"
            

class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
       
class RecordReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"      
        
class RequestLoanForm(forms.ModelForm):
    class Meta:
        model=  Loan
        fields = "__all__"
        
class RecordRewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"        
       
        