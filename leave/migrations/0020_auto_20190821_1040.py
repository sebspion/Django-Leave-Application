# Generated by Django 2.1.10 on 2019-08-21 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0019_leave_dept_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='dept_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
