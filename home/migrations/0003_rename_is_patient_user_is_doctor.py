# Generated by Django 3.2.8 on 2022-07-30 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_is_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_patient',
            new_name='is_doctor',
        ),
    ]