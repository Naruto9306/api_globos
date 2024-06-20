# Generated by Django 5.0.6 on 2024-06-12 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globos', '0025_evento_aprobado_alter_globos_colorglobos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='idarco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globos.narco'),
        ),
        migrations.AlterField(
            model_name='globos',
            name='colorglobos',
            field=models.CharField(choices=[('3', 'Verde'), ('4', 'Amarillo'), ('7', 'Rosa'), ('11', 'Negro'), ('5', 'Azul'), ('2', 'Rojo'), ('9', 'Marrón'), ('10', 'Gris'), ('1', 'Blanco'), ('6', 'Naranja'), ('8', 'Púrpura')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='globos',
            name='formaglobos',
            field=models.CharField(choices=[('2', 'Mediano'), ('3', 'Grande'), ('1', 'Chiquito'), ('4', 'Extragrande')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mes',
            name='descripcion',
            field=models.CharField(choices=[('11', 'Noviembre'), ('6', 'Junio'), ('8', 'Agosto'), ('9', 'Septiembre'), ('3', 'Marzo'), ('10', 'Octubre'), ('4', 'Abril'), ('7', 'Julio'), ('5', 'Mayo'), ('2', 'Febrero'), ('12', 'Diciembre'), ('1', 'Enero')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='narco',
            name='descripcion',
            field=models.CharField(choices=[('1', 'Globos'), ('4', 'Tela'), ('2', 'Flores'), ('3', 'Luminarias')], max_length=15),
        ),
        migrations.AlterField(
            model_name='nbase',
            name='descripcion',
            field=models.CharField(choices=[('3', 'Cilindro'), ('1', 'Corazón'), ('2', 'Cubo'), ('4', 'Cilindro medio')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncubiertos',
            name='descripcion',
            field=models.CharField(choices=[('2', 'Platos'), ('1', 'Vasos'), ('3', 'Servilletas')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ntematica',
            name='descripcion',
            field=models.CharField(choices=[('2', 'Boda'), ('3', 'Revelación de sexo'), ('1', 'Cumpleaños'), ('4', 'Baby shawers'), ('7', '14 de febrero'), ('8', 'Día San Valentín'), ('9', 'Compromiso'), ('6', 'Aniversario de boda'), ('5', 'Graduación')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='colorpinata',
            field=models.CharField(choices=[('3', 'Verde'), ('4', 'Amarillo'), ('7', 'Rosa'), ('11', 'Negro'), ('5', 'Azul'), ('2', 'Rojo'), ('9', 'Marrón'), ('10', 'Gris'), ('1', 'Blanco'), ('6', 'Naranja'), ('8', 'Púrpura')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='formapinata',
            field=models.CharField(choices=[('3', 'Redondo'), ('4', 'Corazón'), ('2', 'Rectangular'), ('1', 'Cuadrado')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionProd',
            field=models.CharField(choices=[('5', 'Centro de mesa'), ('2', 'Arcos'), ('4', 'Piñata'), ('6', 'Cubiertos'), ('1', 'Globos'), ('3', 'Cartel'), ('7', 'Base')], max_length=50),
        ),
    ]
