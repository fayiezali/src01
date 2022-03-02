# Generated by Django 3.2.6 on 2021-12-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_association_months_model_am_monthname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association_months_model',
            name='AM_MonthName',
            field=models.CharField(choices=[('01-January__Jumada Al-Awwal-(05)', '01-January__Jumada Al-Awwal-(05)'), ('02-February_Jumada Al-Thani-(06)', '02-February_Jumada Al-Thani-(06)'), ('03-March______________Rajab-(07)', '03-March______________Rajab-(07)'), ('04-April_____________Shaban-(08)', '04-April_____________Shaban-(08)'), ('05-May______________Ramadan-(09)', '05-May______________Ramadan-(09)'), ('06-June_____________Shawwal-(10)', '06-June_____________Shawwal-(10)'), ('07-July__________Dhul-Qadah-(11)', '07-July__________Dhul-Qadah-(11)'), ('08-August_______Dhul-Hijjah-(12)', '08-August_______Dhul-Hijjah-(12)'), ('09-September_______Muharram-(01)', '09-September_______Muharram-(01)'), ('10-October____________Safar-(02)', '10-October____________Safar-(02)'), ('11-November___Rabi Al-Awwal-(03)', '11-November___Rabi Al-Awwal-(03)'), ('12-December___Rabi Al-Thani-(04)', '12-December___Rabi Al-Thani-(04)')], db_index=True, default='01-January__Jumada Al-Awwal-(05)', max_length=50, verbose_name='إسم الشهر'),
        ),
    ]
