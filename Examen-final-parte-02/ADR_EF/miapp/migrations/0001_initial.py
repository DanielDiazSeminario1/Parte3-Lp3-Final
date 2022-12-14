# Generated by Django 4.0.6 on 2022-08-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(max_length=2)),
                ('nombre', models.TextField()),
                ('precio_compra', models.TextField()),
                ('precio_venta', models.TextField()),
                ('fecha_compra', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
