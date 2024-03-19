from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from .managers import CustomUserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = RegexValidator(regex=r'^[0-9]+$', message='Username must be a long integer.')

    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[username_validator],
        help_text="a numeric username with maximum length 20 characters",
        verbose_name='یوزرنیم/کد ملی'
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = jmodels.jDateTimeField(default=jmodels.timezone.now(), verbose_name='تاریخ عضویت')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Professor(models.Model):
    user = models.ForeignKey(User, related_name='professor', on_delete=models.CASCADE, verbose_name='یوزر')
    professor_code = models.CharField(max_length=20, unique=True, null=False, db_index=True,
                                      verbose_name='شماره استادی')
    first_name = models.CharField(max_length=120, null=False, verbose_name='نام')
    last_name = models.CharField(max_length=120, null=False, verbose_name='نام خانوادگی')
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=10, null=False, choices=GENDERS, verbose_name='جنیست')

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.user.username} - {self.professor_code}"

    class Meta:
        verbose_name = 'استاد'
        verbose_name_plural = 'اساتید'


class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE, verbose_name='یوزر')
    student_code = models.CharField(max_length=20, unique=True, null=False, db_index=True,
                                    verbose_name='شماره دانشجویی')
    first_name = models.CharField(max_length=120, null=False, verbose_name='نام')
    last_name = models.CharField(max_length=120, null=False, verbose_name='نام خانوادگی')
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=10, null=False, choices=GENDERS, verbose_name='جنیست')

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.user.username} - {self.student_code}"

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'
