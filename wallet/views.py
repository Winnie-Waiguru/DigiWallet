from django.shortcuts import render
from .forms import CurrencyChoiceForm, CustomerRegistrationForm, NotificationsForm, RecordReceiptForm, RecordRewardForm, RegisterAccountForm, RegisterCardForm, RegisterThirdparty, RegisterWalletForm, RequestLoanForm, TransactionForm

# Find out the contents of a http response
# Injecting data in a http request you put it in a dictionary
# Create your views here.

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html", {"form": form})
       
    
def choose_currency(request):
    form = CurrencyChoiceForm()
    return render(request,"wallet/choose_currency.html", {"form":form})

def register_wallet(request):
    form = RegisterWalletForm()
    return render(request, "wallet/register_wallet.html", {"form":form})

def register_account(request):
    form = RegisterAccountForm()
    return render(request,"wallet/register_account.html",{"form":form})

def record_transaction(request):
    form  = TransactionForm()
    return render(request,"wallet/record_transaction.html",{"form":form})

def register_card(request):
    form = RegisterCardForm()
    return render(request, "wallet/register_card.html", {"form":form})

def register_thirdparty(request):
    form = RegisterThirdparty()
    return render(request, "wallet/record_thirdparty_details.html", {"form":form})

def record_notifications(request):
    form = NotificationsForm()
    return render(request, "wallet/record_notifications.html", {"form":form})

def record_receipts(request):
    form = RecordReceiptForm()
    return render(request, "wallet/record_receipt.html", {"form":form})

def request_loan(request):
    form = RequestLoanForm()
    return render(request, "wallet/request_loan.html", {"form":form})

def record_reward(request):
    form = RecordRewardForm()
    return render(request, "wallet/record_reward.html",{"form":form})