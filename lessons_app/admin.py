from django.contrib import admin
from .models import (
    Lesson,
    Semester,
    Week,
    LessonPresented,
    PresentingLesson,
    TakingLesson,
    Classroom,
    TeachingTime,
)

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Semester)
admin.site.register(Week)
admin.site.register(LessonPresented)
admin.site.register(PresentingLesson)
admin.site.register(TakingLesson)
admin.site.register(Classroom)
admin.site.register(TeachingTime)
