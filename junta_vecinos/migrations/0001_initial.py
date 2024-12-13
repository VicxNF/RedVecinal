# Generated by Django 5.1 on 2024-08-25 04:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vecino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudCertificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], default='pendiente', max_length=10)),
                ('motivo', models.TextField()),
                ('foto_carnet_frente', models.ImageField(upload_to='carnets/')),
                ('foto_carnet_atras', models.ImageField(upload_to='carnets/')),
                ('documento_residencia', models.FileField(upload_to='documentos_residencia/')),
                ('vecino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junta_vecinos.vecino')),
            ],
        ),
        migrations.CreateModel(
            name='CertificadoResidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('numero_certificado', models.CharField(max_length=20, unique=True)),
                ('documento_certificado', models.FileField(blank=True, null=True, upload_to='certificados/')),
                ('vecino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junta_vecinos.vecino')),
            ],
        ),
    ]