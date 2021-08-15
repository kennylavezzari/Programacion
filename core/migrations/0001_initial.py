# Generated by Django 3.2.4 on 2021-08-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acercade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('fecharegistro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecategoria', models.CharField(max_length=100)),
                ('fecharegistro', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
