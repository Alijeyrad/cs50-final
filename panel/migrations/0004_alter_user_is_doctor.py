# Generated by Django 3.2.8 on 2022-07-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_rename_is_patient_user_is_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
