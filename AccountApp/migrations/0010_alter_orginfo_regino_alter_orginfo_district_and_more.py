# Generated by Django 4.1.3 on 2022-11-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0009_govempinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orginfo',
            name='RegiNo',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='orginfo',
            name='district',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='orginfo',
            name='division',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='orginfo',
            name='org_type',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='orginfo',
            name='upazilla',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='pharinfo',
            name='RegiNo',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pharinfo',
            name='district',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='pharinfo',
            name='division',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='pharinfo',
            name='org_type',
            field=models.CharField(blank=True, choices=[('B.Pharm(A)', 'B.Pharm(A)'), ('Diploma in pharmacy(B)', 'Diploma in pharmacy(B)'), ('Pharmacy Technician(C)', 'Pharmacy Technician(C)')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='pharinfo',
            name='upazilla',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
