# Generated by Django 2.1.10 on 2019-08-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0012_auto_20190814_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(choices=[('sick', 'Sick leave'), ('vacation', 'Vacation leave'), ('end of employee', 'End of Employee leave'), ('maternity', 'Maternity Leave')], default='sick', max_length=30, null=True),
        ),
    ]