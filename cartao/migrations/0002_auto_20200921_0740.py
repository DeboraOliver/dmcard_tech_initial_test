# Generated by Django 3.1.1 on 2020-09-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='renda',
            field=models.CharField(max_length=7, verbose_name='Renda'),
        ),
    ]