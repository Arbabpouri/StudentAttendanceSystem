from django.db import models
from django_jalali.db import models as jmodels


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


