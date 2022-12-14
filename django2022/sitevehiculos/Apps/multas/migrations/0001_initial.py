# Generated by Django 4.1.3 on 2022-11-14 20:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutivoDeMultas', models.CharField(help_text='Ingrese el Consecutivo de Multa', max_length=100)),
                ('fechaYHora', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Actual')),
                ('lugarInfracion', models.CharField(help_text='Ingrese el lugar de la Infración', max_length=100)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.persona', verbose_name='Persona')),
            ],
            options={
                'verbose_name': 'multa',
                'verbose_name_plural': 'multas',
            },
        ),
    ]
