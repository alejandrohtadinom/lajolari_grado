# Generated by Django 2.0.7 on 2018-07-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20180710_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientquantity',
            name='preparation',
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='propiedad_principal',
            field=models.CharField(choices=[('p', 'Proteina'), ('c', 'Carbohidrato'), ('m', 'Mineral'), ('g', 'Grano'), ('ci', 'Citrico'), ('d', 'Dulce'), ('n', 'Neutro'), ('l', 'Lacteo')], help_text='Caracteristica del alimento', max_length=20),
        ),
    ]
