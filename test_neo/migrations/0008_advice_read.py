# Generated by Django 3.2.8 on 2022-08-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_neo', '0007_remove_advice_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]