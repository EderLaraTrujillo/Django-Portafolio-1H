# Generated by Django 3.2.6 on 2021-09-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HabilidadesUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_habil', models.CharField(max_length=50, verbose_name='Nombre de Habilidad')),
                ('porcen_habil', models.IntegerField(max_length=2, verbose_name='Porcentaje de Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad del Usuario',
                'verbose_name_plural': 'Habilidades del Usuario',
            },
        ),
    ]