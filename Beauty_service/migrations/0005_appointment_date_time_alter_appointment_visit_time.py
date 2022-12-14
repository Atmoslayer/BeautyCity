# Generated by Django 4.1.3 on 2022-12-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beauty_service', '0004_shedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_time',
            field=models.DateField(null=True, verbose_name='Дата посещения'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='visit_time',
            field=models.TimeField(db_index=True, verbose_name='время посещения'),
        ),
    ]
