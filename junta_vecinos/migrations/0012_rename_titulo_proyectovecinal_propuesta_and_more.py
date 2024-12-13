# Generated by Django 5.1 on 2024-10-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junta_vecinos', '0011_reserva_monto_pagado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectovecinal',
            old_name='titulo',
            new_name='propuesta',
        ),
        migrations.RemoveField(
            model_name='proyectovecinal',
            name='archivo_propuesta',
        ),
        migrations.AddField(
            model_name='proyectovecinal',
            name='evidencia',
            field=models.ImageField(blank=True, null=True, upload_to='evidencias/'),
        ),
        migrations.AddField(
            model_name='proyectovecinal',
            name='razon_rechazo',
            field=models.TextField(blank=True, null=True),
        ),
    ]