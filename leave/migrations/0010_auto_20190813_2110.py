# Generated by Django 2.1.10 on 2019-08-13 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0009_auto_20190813_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='accepted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leaves_to', to=settings.AUTH_USER_MODEL),
        ),
    ]