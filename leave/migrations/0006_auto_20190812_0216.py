# Generated by Django 2.1.10 on 2019-08-12 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_auto_20190812_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(default='Pending', max_length=12),
        ),
    ]
