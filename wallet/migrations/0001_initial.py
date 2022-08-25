# Generated by Django 4.0.6 on 2022-08-25 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=15, null=True)),
                ('balance', models.PositiveIntegerField()),
                ('account_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_origin', models.CharField(max_length=24, null=True)),
                ('Symbol', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=23, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='female', max_length=15)),
                ('address', models.CharField(max_length=23, null=True)),
                ('age', models.SmallIntegerField(null=True)),
                ('nationality', models.CharField(max_length=15, null=True)),
                ('id_number', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('profile_picture', models.ImageField(default=False, upload_to='')),
                ('signature', models.ImageField(default=False, upload_to='')),
                ('employed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=15, null=True)),
                ('pin', models.TextField(max_length=8, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=15, null=True)),
                ('transaction_charge', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=datetime.datetime.now)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipt', to='wallet.account')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipt', to='wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('thirdparty_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Third_party_account', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('customer_id', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bonus', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_date', models.DateField(default=datetime.datetime.now)),
                ('receipt_file', models.FileField(upload_to='')),
                ('total_amount', models.PositiveIntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_transaction', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications_id', models.IntegerField()),
                ('name', models.CharField(max_length=15, null=True)),
                ('status', models.CharField(max_length=15, null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_receipt', to='wallet.third_party')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=15, null=True)),
                ('amount', models.IntegerField()),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('interest_rate', models.IntegerField()),
                ('pay_due_date', models.DateTimeField(default='')),
                ('loan_balance', models.IntegerField()),
                ('guarantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guarantor', to='wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateTimeField(default=datetime.datetime.now)),
                ('card_name', models.CharField(max_length=15, null=True)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(max_length=15, null=True)),
                ('exipry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('card_status', models.CharField(max_length=15, null=True)),
                ('security_code', models.IntegerField()),
                ('signature', models.ImageField(upload_to='')),
                ('issuer', models.CharField(max_length=15, null=True)),
                ('Wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='wallet.account')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
