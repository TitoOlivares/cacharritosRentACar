# Generated by Django 2.2.6 on 2019-10-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191026_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
