# Generated by Django 5.1 on 2024-09-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junta_vecinos', '0005_alter_certificadoresidencia_documento_certificado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudcertificado',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=10),
        ),
    ]
