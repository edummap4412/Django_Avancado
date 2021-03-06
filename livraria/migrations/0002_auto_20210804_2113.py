# Generated by Django 2.1.7 on 2021-08-05 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.FloatField()),
                ('media', models.DecimalField(decimal_places=2, max_digits=10)),
                ('authors', models.ManyToManyField(to='livraria.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livraria.Publisher')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='media',
        ),
    ]
