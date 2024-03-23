from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from users_app.models import Professor, Student
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Lesson(models.Model):
    course_number = models.BigIntegerField(null=False, db_index=True, verbose_name='کد درس')
    course_title = models.CharField(max_length=120, null=False, verbose_name='نام درس')
    number_of_unit = models.IntegerField(null=False, db_index=True, verbose_name='تعداد واحد')

    def __str__(self):
        return f'{self.course_title} - {self.course_number} - {self.number_of_unit}'

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'


class Semester(models.Model):
    semester_number = models.BigIntegerField(null=False, db_index=True, verbose_name='کد ترم')
    semester_title = models.CharField(max_length=120, verbose_name='نام ترم')
    semester_year = jmodels.jDateTimeField(default=jmodels.timezone.now(), verbose_name='تاریخ')

    def __str__(self):
        return self.semester_title

    class Meta:
        verbose_name = 'ترم'
        verbose_name_plural = 'ترم ها'


class Week(models.Model):
    week_number = models.BigIntegerField(null=False, db_index=True, verbose_name='کد هفته')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='weeks', verbose_name='ترم')
    week_start = ...
    week_end = ...

    def __str__(self):
        return f'{self.week_number} - {self.semester.semester_title}'

    class Meta:
        verbose_name = 'هفته'
        verbose_name_plural = 'هفته ها'


class LessonPresented(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name='lesson_presented',
        verbose_name='ترم'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='lesson_presented',
        verbose_name='درس'
    )
    group_number = models.IntegerField(verbose_name='شماره گروه')

    def __str__(self):
        return f"{self.semester.semester_title} - {self.lesson.course_title} - {self.group_number}"

    class Meta:
        verbose_name = 'درس ارائه شده'
        verbose_name_plural = 'دروس ارائه شده'


class PresentingLesson(models.Model):
    lesson_presented = models.ForeignKey(
        LessonPresented,
        on_delete=models.CASCADE,
        related_name='presenting_lesson',
        verbose_name='درس ارائه شده'
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='presenting_lesson',
        verbose_name='استاد'
    )

    def __str__(self):
        return f""

    class Meta:
        verbose_name = 'ارائه دادن درس'
        verbose_name_plural = 'ارائه دادن دروس'


class TakingLesson(models.Model):
    lesson_presented = models.ForeignKey(
        LessonPresented,
        on_delete=models.CASCADE,
        related_name='taking_lesson',
        verbose_name='درس ارائه شده'
    )
    professor = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='taking_lesson',
        verbose_name='دانشجو'
    )

    def __str__(self):
        return f""

    class Meta:
        verbose_name = 'اخذ کردن درس'
        verbose_name_plural = 'اخذ کردن دروس'


class Classroom(models.Model):
    session_number = models.IntegerField(verbose_name='شماره جلسه')
    session_day_number = models.IntegerField(
        verbose_name='شماره روز بین 0 تا 6',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(6)
        ]
    )

    session_start_time = models.TimeField(verbose_name='ساعت شروع', default=timezone.now())
    session_start_time = models.TimeField(verbose_name='ساعت پایان')

    def __str__(self):
        return f""

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'


class TeachingTime(models.Model):
    lesson = models.ForeignKey(
        LessonPresented,
        on_delete=models.CASCADE,
        related_name='teaching_time',
        verbose_name='درس'
    )

    session = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='teaching_time',
        verbose_name='کلاس'
    )

    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE,
        related_name='teaching_time',
        verbose_name='هفته'
    )

    def __str__(self):
        return f""

    class Meta:
        verbose_name = 'زمان ارائه درس'
        verbose_name_plural = 'زمان ارائه دروس'
