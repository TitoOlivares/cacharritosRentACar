# Generated by Django 2.2.6 on 2019-10-26 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automovil',
            options={'verbose_name': 'Automovil', 'verbose_name_plural': 'Automoviles'},
        ),
        migrations.AlterField(
            model_name='automovil',
            name='agno',
            field=models.IntegerField(verbose_name='año'),
        ),
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(default='', max_length=9)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('fecha_arriendo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
