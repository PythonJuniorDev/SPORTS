# Generated by Django 4.1.7 on 2023-03-10 08:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_instructor', models.CharField(choices=[('Raymond', 'Raymond'), ('Doff', 'Doff'), ('Toon', 'Toon'), ('Patrick', 'Patrick')], default='Toon', max_length=10)),
                ('permanent_contract', models.BooleanField()),
                ('zero_hours_contract', models.BooleanField()),
                ('on_call_basis', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal_access_code',
            fields=[
                ('id', models.UUIDField(db_column='Personal access code', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='personal access code+', to='athletes.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('X', 'Gender Neutral')], default='X', max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('birth_date', models.DateField(null=True)),
                ('contact_person', models.CharField(default=True, max_length=80)),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1)),
                ('date_registered', models.DateTimeField(default=datetime.datetime.now)),
                ('group_lessons', models.CharField(choices=[('Fitness', 'Fitness'), ('Spinning', 'Spinning'), ('Boxing', 'Boxing'), ('Zumba', 'Zumba'), ('Krav maga', 'Krav Maga'), ('Cross Camp', 'Cross Camp'), ('HITT', 'High Intensity Training'), ('Pilates', 'Pilates'), ('Salsa', 'Salsa'), ('Yoga', 'Yoga')], default=None, max_length=60)),
                ('trial_lesson', models.BooleanField(default=False)),
                ('free_drink', models.BooleanField(default=False)),
                ('member', models.BooleanField()),
                ('instructor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='athlete', to='athletes.instructor')),
            ],
        ),
    ]
