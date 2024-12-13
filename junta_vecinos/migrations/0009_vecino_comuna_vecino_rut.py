# Generated by Django 5.1 on 2024-10-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junta_vecinos', '0008_espacio_foto_espacio_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='vecino',
            name='comuna',
            field=models.CharField(choices=[('ÑUÑOA', 'Ñuñoa'), ('PUENTE_ALTO', 'Puente Alto'), ('LA_FLORIDA', 'La Florida')], default='Ñuñoa', max_length=20),
        ),
        migrations.AddField(
            model_name='vecino',
            name='rut',
            field=models.CharField(default=0, max_length=12, unique=True),
            preserve_default=False,
        ),
    ]