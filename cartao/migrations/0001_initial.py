# Generated by Django 3.1.1 on 2020-09-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254)),
                ('renda', models.FloatField(verbose_name='Renda')),
                ('pedido_em', models.DateTimeField(auto_now_add=True, verbose_name='pedido_em')),
            ],
        ),
    ]
