# Generated by Django 4.0.3 on 2022-07-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia_Arte', '0012_profesores'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores',
            name='biografia_profesor',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='descripcion_profesor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
