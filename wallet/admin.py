from django.contrib import admin

from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.
admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)