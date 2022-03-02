# Generated by Django 3.2.6 on 2021-12-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20211220_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_menu',
            fields=[
                ('m_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_menu_name', models.CharField(max_length=50)),
                ('m_menu_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sub_menu',
            fields=[
                ('s_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_menu_id', models.IntegerField()),
                ('s_menu_name', models.CharField(max_length=50)),
                ('s_menu_link', models.CharField(max_length=100)),
            ],
        ),
    ]
