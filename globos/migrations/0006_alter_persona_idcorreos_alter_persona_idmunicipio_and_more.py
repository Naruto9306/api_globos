# Generated by Django 5.0.6 on 2024-06-02 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globos', '0005_alter_persona_idcorreos_alter_persona_idmunicipio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='idcorreos',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='globos.correos'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='idmunicipio',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='globos.municipio'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='idpais',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='globos.pais'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='idprovincia',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='globos.provincia'),
        ),
    ]
