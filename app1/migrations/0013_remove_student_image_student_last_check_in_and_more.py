# Generated by Django 5.0.7 on 2024-11-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_bus_driver_name_bus_driver_phone_alter_bus_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='student',
            name='last_check_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_check_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=50),
        ),
    ]