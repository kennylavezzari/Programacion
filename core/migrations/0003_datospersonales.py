# Generated by Django 3.2.4 on 2021-08-14 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contacto_inicio_menu_portada_portafolios'),
    ]

    operations = [
        migrations.CreateModel(
            name='datospersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
