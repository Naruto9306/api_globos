# Generated by Django 5.0.6 on 2024-06-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globos', '0019_alter_globos_colorglobos_alter_globos_formaglobos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='globos',
            name='colorglobos',
            field=models.CharField(choices=[('9', 'Marrón'), ('7', 'Rosa'), ('4', 'Amarillo'), ('8', 'Púrpura'), ('2', 'Rojo'), ('3', 'Verde'), ('10', 'Gris'), ('6', 'Naranja'), ('1', 'Blanco'), ('11', 'Negro'), ('5', 'Azul')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='globos',
            name='formaglobos',
            field=models.CharField(choices=[('2', 'Mediano'), ('4', 'Extragrande'), ('3', 'Grande'), ('1', 'Chiquito')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mes',
            name='descripcion',
            field=models.CharField(choices=[('3', 'Marzo'), ('9', 'Septiembre'), ('5', 'Mayo'), ('6', 'Junio'), ('1', 'Enero'), ('4', 'Abril'), ('11', 'Noviembre'), ('12', 'Diciembre'), ('7', 'Julio'), ('10', 'Octubre'), ('2', 'Febrero'), ('8', 'Agosto')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='narco',
            name='descripcion',
            field=models.CharField(choices=[('2', 'Flores'), ('3', 'Luminarias'), ('1', 'Globos'), ('4', 'Tela')], max_length=15),
        ),
        migrations.AlterField(
            model_name='nbase',
            name='descripcion',
            field=models.CharField(choices=[('3', 'Cilindro'), ('2', 'Cubo'), ('1', 'Corazón'), ('4', 'Cilindro medio')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncentromesa',
            name='descripcion',
            field=models.CharField(choices=[('1', 'Adornos'), ('2', 'Dulces')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncubiertos',
            name='descripcion',
            field=models.CharField(choices=[('2', 'Platos'), ('1', 'Vasos'), ('3', 'Servilletas')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ntematica',
            name='descripcion',
            field=models.CharField(choices=[('5', 'Graduación'), ('3', 'Revelación de sexo'), ('1', 'Cumpleaños'), ('2', 'Boda'), ('8', 'Día San Valentín'), ('4', 'Baby shawers'), ('6', 'Aniversario de boda'), ('7', '14 de febrero'), ('9', 'Compromiso')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='colorpinata',
            field=models.CharField(choices=[('9', 'Marrón'), ('7', 'Rosa'), ('4', 'Amarillo'), ('8', 'Púrpura'), ('2', 'Rojo'), ('3', 'Verde'), ('10', 'Gris'), ('6', 'Naranja'), ('1', 'Blanco'), ('11', 'Negro'), ('5', 'Azul')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='formapinat',
            field=models.CharField(choices=[('1', 'Cuadrado'), ('4', 'Corazón'), ('3', 'Redondo'), ('2', 'Rectangular')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionProd',
            field=models.CharField(choices=[('6', 'Cubiertos'), ('1', 'Globos'), ('3', 'Cartel'), ('5', 'Centro de mesa'), ('7', 'Base'), ('2', 'Arcos'), ('4', 'Piñata')], max_length=50),
        ),
    ]
