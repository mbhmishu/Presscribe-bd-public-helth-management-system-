# Generated by Django 4.1.3 on 2022-11-29 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AccountApp', '0012_delete_verify'),
        ('managment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verify',
            name='expecting',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='expecting_ac', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='verify',
            name='toverify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_verify', to='AccountApp.govempinfo'),
        ),
    ]
