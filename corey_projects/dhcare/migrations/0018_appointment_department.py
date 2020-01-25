# Generated by Django 3.0.2 on 2020-01-24 10:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dhcare', '0017_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('nid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('department_code',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhcare.department')),
            ],
        ),
    ]