# Generated by Django 5.0.7 on 2025-01-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_student_last_update_time_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='arduino_port',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
