# Generated by Django 3.2.6 on 2021-12-07 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_association_months_model_am_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association_months_model',
            name='AM_MonthNumber',
        ),
    ]
