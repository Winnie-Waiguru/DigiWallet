from django.contrib import admin

from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","email")
    search_fields= ("first_name","last_name")
admin.site.register(Customer)

class CurrencyAdmin(admin.ModelAdmin):
    list_display =("country_of_origin","symbol")
    search_fields= ("country_of_origin","symbol")
admin.site.register(Currency)

class WalletAdmin(admin.ModelAdmin):
    list_display =("currency","customer")
    search_fields= ("currency","customer")
admin.site.register(Wallet)

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_type","balance")
    search_fields= ("account_type","balance")
admin.site.register(Account)

class TransactionAdmin(admin.ModelAdmin):
    list_display =("wallet","transaction_amount")
    search_fields= ("wallet","transaction_amount")
admin.site.register(Transaction)

class CardAdmin(admin.ModelAdmin):
    list_display =("date_issued","card_name")
    search_fields= ("date_issued","card_name")
admin.site.register(Card)

class Third_partyAdmin(admin.ModelAdmin):
    list_display =("account","name")
    search_fields= ("account","name")
admin.site.register(Third_party)

class NotificationAdmin(admin.ModelAdmin):
    list_display =("notifications_id","name")
    search_fields= ("notifications_id","name")
admin.site.register(Notification)

class ReceiptAdmin(admin.ModelAdmin):
    list_display =("receipt_date","receipt_file")
    search_fields= ("receipt_date","receipt_file")
admin.site.register(Receipt)

class LoanAdmin(admin.ModelAdmin):
    list_display =("loan_type","amount")
    search_fields= ("loan_type","amount")
admin.site.register(Loan)

class RewardAdmin(admin.ModelAdmin):
    list_display =("transaction","date_and_time")
    search_fields= ("transaction","date_and_time")
admin.site.register(Reward)