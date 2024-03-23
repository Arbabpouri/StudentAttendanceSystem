# Generated by Django 5.0.3 on 2024-03-23 07:50

import datetime
import django.core.validators
import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_number', models.IntegerField(verbose_name='شماره جلسه')),
                ('session_day_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)], verbose_name='شماره روز بین 0 تا 6')),
                ('session_start_time', models.TimeField(verbose_name='ساعت پایان')),
            ],
            options={
                'verbose_name': 'کلاس',
                'verbose_name_plural': 'کلاس ها',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.BigIntegerField(db_index=True, verbose_name='کد درس')),
                ('course_title', models.CharField(max_length=120, verbose_name='نام درس')),
                ('number_of_unit', models.IntegerField(db_index=True, verbose_name='تعداد واحد')),
            ],
            options={
                'verbose_name': 'درس',
                'verbose_name_plural': 'دروس',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_number', models.BigIntegerField(db_index=True, verbose_name='کد ترم')),
                ('semester_title', models.CharField(max_length=120, verbose_name='نام ترم')),
                ('semester_year', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2024, 3, 23, 7, 50, 19, 745416, tzinfo=datetime.timezone.utc), verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'ترم',
                'verbose_name_plural': 'ترم ها',
            },
        ),
        migrations.CreateModel(
            name='TakingLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'اخذ کردن درس',
                'verbose_name_plural': 'اخذ کردن دروس',
            },
        ),
        migrations.CreateModel(
            name='TeachingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'زمان ارائه درس',
                'verbose_name_plural': 'زمان ارائه دروس',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.BigIntegerField(db_index=True, verbose_name='کد هفته')),
            ],
            options={
                'verbose_name': 'هفته',
                'verbose_name_plural': 'هفته ها',
            },
        ),
        migrations.CreateModel(
            name='LessonPresented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField(verbose_name='شماره گروه')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_presented', to='lessons_app.lesson', verbose_name='درس')),
            ],
            options={
                'verbose_name': 'درس ارائه شده',
                'verbose_name_plural': 'دروس ارائه شده',
            },
        ),
        migrations.CreateModel(
            name='PresentingLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_presented', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presenting_lesson', to='lessons_app.lessonpresented', verbose_name='درس ارائه شده')),
            ],
            options={
                'verbose_name': 'ارائه دادن درس',
                'verbose_name_plural': 'ارائه دادن دروس',
            },
        ),
    ]
