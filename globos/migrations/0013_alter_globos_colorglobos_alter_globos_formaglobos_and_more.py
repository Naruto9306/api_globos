# Generated by Django 5.0.6 on 2024-06-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globos', '0012_correos_fecharegistro_alter_globos_colorglobos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globos',
            name='colorglobos',
            field=models.CharField(choices=[('5', 'Azul'), ('10', 'Gris'), ('6', 'Naranja'), ('8', 'Púrpura'), ('3', 'Verde'), ('9', 'Marrón'), ('11', 'Negro'), ('2', 'Rojo'), ('7', 'Rosa'), ('4', 'Amarillo'), ('1', 'Blanco')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='globos',
            name='formaglobos',
            field=models.CharField(choices=[('3', 'Grande'), ('1', 'Mediano'), ('0', 'Chiquito'), ('4', 'Extragrande')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mes',
            name='descripcion',
            field=models.CharField(choices=[('11', 'Noviembre'), ('7', 'Julio'), ('9', 'Septiembre'), ('2', 'Febrero'), ('4', 'Abril'), ('8', 'Agosto'), ('10', 'Octubre'), ('5', 'Mayo'), ('3', 'Marzo'), ('6', 'Junio'), ('12', 'Diciembre'), ('1', 'Enero')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='narco',
            name='descripcion',
            field=models.CharField(choices=[('3', 'Tela'), ('2', 'Luminarias'), ('0', 'Globos'), ('1', 'Flores')], max_length=15),
        ),
        migrations.AlterField(
            model_name='nbase',
            name='descripcion',
            field=models.CharField(choices=[('2', 'Cilindro'), ('1', 'Cubo'), ('0', 'Corazón'), ('3', 'Cilindro medio')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncentromesa',
            name='descripcion',
            field=models.CharField(choices=[('0', 'Adornos'), ('1', 'Dulces')], max_length=15),
        ),
        migrations.AlterField(
            model_name='ncubiertos',
            name='descripcion',
            field=models.CharField(choices=[('0', 'Vasos'), ('1', 'Platos'), ('2', 'Servilletas')], max_length=15),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='colorpinata',
            field=models.CharField(choices=[('5', 'Azul'), ('10', 'Gris'), ('6', 'Naranja'), ('8', 'Púrpura'), ('3', 'Verde'), ('9', 'Marrón'), ('11', 'Negro'), ('2', 'Rojo'), ('7', 'Rosa'), ('4', 'Amarillo'), ('1', 'Blanco')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='pinata',
            name='formapinat',
            field=models.CharField(choices=[('3', 'Corazón'), ('1', 'Rectangular'), ('2', 'Redondo'), ('0', 'Cuadrado')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionProd',
            field=models.CharField(choices=[('3', 'Piñata'), ('0', 'Globos'), ('4', 'Centro de mesa'), ('2', 'Cartel'), ('6', 'Base'), ('1', 'Arcos'), ('5', 'Cubiertos')], max_length=50),
        ),
    ]
