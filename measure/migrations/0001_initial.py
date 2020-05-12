# Generated by Django 2.2.5 on 2020-05-12 23:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20, verbose_name='Tipo')),
                ('value', models.IntegerField(verbose_name='Valor')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('codigo', models.IntegerField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('terreno', models.CharField(choices=[('Planicie', 'Planicie'), ('Ladera', 'Ladera'), ('Cenagoso', 'Cenagoso'), ('Desertico', 'Desertico')], max_length=10)),
                ('area', models.PositiveIntegerField()),
            ],
        ),
    ]
