# Generated by Django 3.2 on 2024-03-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='contact',
            field=models.CharField(max_length=128, verbose_name='ФИО'),
        ),
    ]