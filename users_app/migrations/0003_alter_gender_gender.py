# Generated by Django 5.0.3 on 2024-03-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(db_index=True, default=None, editable=False, max_length=20, unique=True),
        ),
    ]
