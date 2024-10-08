# Generated by Django 4.1.7 on 2023-03-10 10:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_alter_personal_access_code_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personal_access_code',
            name='id',
            field=models.UUIDField(db_column='Personal access code', default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
