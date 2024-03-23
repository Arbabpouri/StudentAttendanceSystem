from django.db import models
from lessons_app.models import Classroom, Week, LessonPresented
from users_app.models import Student, Professor


# Create your models here.

class PresenceAbsence(models.Model):
    session = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='presence_absence',
        verbose_name='جلسه'
    )
    week = models.ForeignKey(
        Week,
        on_delete=models.CASCADE,
        related_name='presence_absence',
        verbose_name='هفته'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='presence_absence',
        verbose_name='دانشجو'
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='presence_absence',
        verbose_name='استاد'
    )
    lesson = models.ForeignKey(
        LessonPresented,
        on_delete=models.CASCADE,
        related_name='presence_absence',
        verbose_name='درس'
    )
    roll_call = models.BooleanField(verbose_name='حضور')

    def __str__(self):
        return f""

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
