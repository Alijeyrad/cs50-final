# Generated by Django 3.2.8 on 2022-07-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0015_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='/empty-profile.png', null=True, upload_to='profile_pics'),
        ),
    ]
