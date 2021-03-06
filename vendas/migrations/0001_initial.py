# Generated by Django 2.1.7 on 2021-07-29 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        ('clientes', '0009_auto_20210726_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('nfe_emitida', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
                ('produtos', models.ManyToManyField(blank=True, to='produto.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='itemdopedido',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda'),
        ),
    ]
