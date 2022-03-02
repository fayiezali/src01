# Generated by Django 3.2.6 on 2021-12-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211202_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialdata_model',
            name='FIN_MethodPaymentCash',
        ),
        migrations.RemoveField(
            model_name='financialdata_model',
            name='FIN_MethodPaymentCheck',
        ),
        migrations.RemoveField(
            model_name='financialdata_model',
            name='FIN_MethodPaymentTransfer',
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_SocialStatusMarried',
        ),
        migrations.RemoveField(
            model_name='personaldata_model',
            name='PER_SocialStatusUnmarried',
        ),
        migrations.AddField(
            model_name='financialdata_model',
            name='FIN_MethodReceive',
            field=models.CharField(choices=[('CA', 'Cash'), ('CH', 'Check'), ('TR', 'Transfer')], db_index=True, default='CA', max_length=2, verbose_name='طريقة إستلام قيمة اﻷسهم'),
        ),
        migrations.AlterField(
            model_name='financialdata_model',
            name='FIN_MethodPayment',
            field=models.CharField(choices=[('CA', 'Cash'), ('CH', 'Check'), ('TR', 'Transfer')], db_index=True, default='CA', max_length=2, verbose_name='طريقة سداد قيمة اﻷسهم'),
        ),
    ]
