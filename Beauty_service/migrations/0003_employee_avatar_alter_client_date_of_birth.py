# Generated by Django 4.1.4 on 2022-12-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beauty_service', '0002_alter_employee_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата рождения'),
        ),
    ]