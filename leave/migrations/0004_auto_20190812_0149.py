# Generated by Django 2.1.10 on 2019-08-12 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20190811_2148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leave',
            options={'get_latest_by': 'created', 'ordering': ['-created'], 'verbose_name': 'Leave', 'verbose_name_plural': 'Leaves'},
        ),
    ]
