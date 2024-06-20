# Generated by Django 5.0.6 on 2024-06-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globos', '0016_ntematica_globos_cantidad_globos_precio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globos',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='globos',
            name='precio',
        ),
        migrations.AlterField(
            model_name='globos',
            name='colorglobos',
            field=models.CharField(choices=[('10', 'Gris'), ('1', 'Blanco'), ('6', 'Naranja'), ('8', 'Púrpura'), ('9', 'Marrón'), ('5', 'Azul'), ('3', 'Verde'), ('11', 'Negro'), ('2', 'Rojo'), ('7', 'Rosa'), ('4', 'Amarillo')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mes',
            name='descripcion',
            field=models.CharField(choices=[('9', 'Septiembre'), ('8', 'Agosto'), ('11', 'Noviembre'), ('3', 'Marzo'), ('2', 'Febrero'), ('12', 'Diciembre'), ('10', 'Octubre'), ('7', 'Julio'), ('6', 'Junio'), ('5', 'Mayo'), ('4', 'Abril'), ('1', 'Enero')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='narco',
            name='descripcion',
            field=models.CharField(choices=[('4', 'Tela'), ('3', 'Luminarias'), ('2', 'Flores'), ('1', 'Globos')], max_length=15),
        ),
        migrations.AlterField(
            model_name='nbase',
            name='descripcion',
            field=models.CharField(choices=[('4', 'Cilindro medio'), ('1', 'Corazón'), ('3', 'Cilindro'), ('2', 'Cubo')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncubiertos',
            name='descripcion',
            field=models.CharField(choices=[('3', 'Servilletas'), ('2', 'Platos'), ('1', 'Vasos')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ntematica',
            name='descripcion',
            field=models.CharField(choices=[('6', 'Aniversario de boda'), ('5', 'Graduación'), ('9', 'Compromiso'), ('8', 'Día San Valentín'), ('2', 'Boda'), ('7', '14 de febrero'), ('1', 'Cumpleaños'), ('3', 'Revelación de sexo'), ('4', 'Baby shawers')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='colorpinata',
            field=models.CharField(choices=[('10', 'Gris'), ('1', 'Blanco'), ('6', 'Naranja'), ('8', 'Púrpura'), ('9', 'Marrón'), ('5', 'Azul'), ('3', 'Verde'), ('11', 'Negro'), ('2', 'Rojo'), ('7', 'Rosa'), ('4', 'Amarillo')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='formapinat',
            field=models.CharField(choices=[('1', 'Cuadrado'), ('3', 'Redondo'), ('2', 'Rectangular'), ('4', 'Corazón')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionProd',
            field=models.CharField(choices=[('5', 'Centro de mesa'), ('3', 'Cartel'), ('2', 'Arcos'), ('1', 'Globos'), ('7', 'Base'), ('4', 'Piñata'), ('6', 'Cubiertos')], max_length=50),
        ),
    ]
