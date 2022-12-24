# Generated by Django 2.2.12 on 2022-11-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'verbose_name': 'Aplikācija nosaukums', 'verbose_name_plural': 'Aplikācijas nosaukums'},
        ),
        migrations.CreateModel(
            name='incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Incidenta nosaukums')),
                ('message', models.TextField(verbose_name='Incidenta apraksts')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidentapp.component')),
            ],
            options={
                'verbose_name': 'Incidenta nosaukums',
                'verbose_name_plural': 'Incidentas nosaukums',
                'ordering': ['name'],
            },
        ),
    ]