# Generated by Django 3.1 on 2024-09-10 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('DNI', models.IntegerField(verbose_name='DNI')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('fechan', models.DateField(verbose_name='Fecha Nacimiento')),
                ('altura', models.FloatField(max_length=3, verbose_name='Altura')),
                ('peso', models.FloatField(max_length=3, verbose_name='Peso')),
                ('dire', models.CharField(max_length=50, verbose_name='Direccion')),
                ('cd', models.CharField(max_length=6, verbose_name='codigo postal')),
                ('talla', models.CharField(max_length=6, verbose_name='numero de talla indumentaria')),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugadores.deporte', verbose_name='descripcion')),
            ],
        ),
    ]
