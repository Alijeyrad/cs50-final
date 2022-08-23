# Generated by Django 3.2.8 on 2022-08-23 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_neo', '0004_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advice_giver', to=settings.AUTH_USER_MODEL)),
                ('test_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
