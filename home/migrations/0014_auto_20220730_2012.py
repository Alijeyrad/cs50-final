# Generated by Django 3.2.8 on 2022-07-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_user_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='home_town',
            new_name='city',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/empty-profile.png', upload_to='profile_pics'),
        ),
    ]