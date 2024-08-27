# Generated by Django 3.1 on 2024-08-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocioCuota',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('DNI', models.IntegerField(verbose_name='DNI')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('fechaMes', models.DateField(verbose_name='Fecha Mes a abonar')),
                ('fechap', models.DateField(verbose_name='Fecha pago')),
                ('tel', models.CharField(max_length=15, verbose_name='telefono')),
                ('imp', models.FloatField(verbose_name='importe')),
            ],
        ),
    ]
