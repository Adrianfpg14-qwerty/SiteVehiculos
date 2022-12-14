# Generated by Django 4.1.3 on 2022-11-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='DNI')),
                ('nombre', models.CharField(help_text='Ingrese el Nombre de la Persona', max_length=100)),
                ('apellidos', models.CharField(help_text='Ingrese el Apellido de la Persona', max_length=100)),
                ('direccion', models.CharField(help_text='Ingrese la Direccion de la Persona', max_length=100)),
                ('telefono', models.CharField(help_text='Ingrese el Telefono de la Persona', max_length=12)),
                ('ciudad', models.CharField(help_text='Ingrese la ciudad de la Persona', max_length=100)),
                ('tipoDePersonas', models.CharField(help_text='Ingrese el Tipo de Persona (Natural/Juridica)', max_length=100)),
            ],
            options={
                'verbose_name': 'persona',
                'verbose_name_plural': 'personas',
            },
        ),
    ]
