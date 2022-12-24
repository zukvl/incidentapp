# Generated by Django 2.2.12 on 2022-11-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentapp', '0003_auto_20221118_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'verbose_name': 'Aplikācija', 'verbose_name_plural': 'Aplikācijas'},
        ),
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ['name'], 'verbose_name': 'Incidents', 'verbose_name_plural': 'Incidents'},
        ),
        migrations.AlterField(
            model_name='incident',
            name='message',
            field=models.TextField(verbose_name='Paziņojums'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Temats'),
        ),
    ]
