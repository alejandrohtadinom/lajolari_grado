# Generated by Django 2.0.7 on 2018-07-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20180717_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='tipo',
            field=models.CharField(default='Desayuno', help_text='Ingrese un tipo de Receta', max_length=20),
        ),
    ]
