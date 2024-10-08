# Generated by Django 5.1 on 2024-08-26 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComponentName', models.CharField(choices=[('hw', 'Height/weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')], max_length=20)),
                ('ComponentValue', models.CharField(max_length=20)),
                ('MeasuredDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.patient')),
            ],
        ),
    ]
