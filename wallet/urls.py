from atexit import register
from django.urls import path
from .views import record_notifications, record_reward,record_transaction, register_card, register_customer, choose_currency, register_thirdparty, register_wallet,register_account,record_receipts,request_loan


urlpatterns = [
    path("register/", register_customer, name="registration"),
    path("currency/", choose_currency, name="currency"),
    path("wallets/", register_wallet, name="walletregistration"),
    path("account/", register_account, name="walletregistration"),
    path("transaction/", record_transaction, name="transactionrecordings"),
    path("card/", register_card, name="cardregistration"),
    path("third_party/",register_thirdparty, name="thirdpartydetails"),
    path("notification/",record_notifications, name="notificationsrecord"),
    path("receipt/", record_receipts, name= "receiptrecord"),
    path("loan/", request_loan, name="loanrequesting"),
    path("reward/", record_reward, name="recordingreward"),
    
               ]