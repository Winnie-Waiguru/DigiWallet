# Generated by Django 4.0.6 on 2022-08-29 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_rename_symbol_currency_symbol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Wallet',
            new_name='wallet',
        ),
    ]
