# Generated by Django 5.1.2 on 2024-10-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='Nimap_Client',
        ),
        migrations.AlterModelTable(
            name='project',
            table='Nimap_Project',
        ),
    ]
