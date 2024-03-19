# Generated by Django 5.0.3 on 2024-03-19 15:20

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_number', models.BigIntegerField(db_index=True, verbose_name='کد ترم')),
                ('semester_title', models.CharField(max_length=120, verbose_name='نام ترم')),
                ('semester_year', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'ترم',
                'verbose_name_plural': 'ترم ها',
            },
        ),
    ]
