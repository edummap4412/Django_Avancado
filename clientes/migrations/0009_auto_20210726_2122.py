# Generated by Django 2.1.7 on 2021-07-27 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_itensdopedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itensdopedido',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='itensdopedido',
            name='venda',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.DeleteModel(
            name='ItensDoPedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
