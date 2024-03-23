# Generated by Django 5.0.3 on 2024-03-23 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresenceAbsence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_call', models.BooleanField(verbose_name='حضور')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presence_absence', to='lessons_app.lessonpresented', verbose_name='درس')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
