# Generated by Django 3.1.2 on 2020-10-29 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=25, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=25, verbose_name='Apellido Materno')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('curp', models.CharField(max_length=18, verbose_name='C.U.R.P.')),
                ('rfc', models.CharField(max_length=13, verbose_name='R.F.C.')),
                ('num_empleado', models.CharField(max_length=20, unique=True, verbose_name='N° Empleado')),
                ('num_plaza', models.CharField(max_length=20, verbose_name='N° Plaza')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de Ingreso')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('codigo_puesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.codigopuesto')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.hospital')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.nivelsalarial')),
                ('prestaciones', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.prestaciones')),
                ('secc_sindical', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.seccionsindical')),
                ('tipo_contratacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.tipocontratacion')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.turno')),
                ('universo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.universo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('zona_pagadora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admins.zonapagadora')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
                'ordering': ['apellido_paterno'],
                'unique_together': {('num_empleado',)},
            },
        ),
    ]
