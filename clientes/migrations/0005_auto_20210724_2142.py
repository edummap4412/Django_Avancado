# Generated by Django 2.1.7 on 2021-07-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210724_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(blank=True, to='clientes.Produto'),
        ),
    ]
