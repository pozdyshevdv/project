from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    # Модель представляющая резюме
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    worker_cover = models.ImageField(upload_to='images/', default='images/user.png')
    first_name = models.CharField(max_length=256, verbose_name='Имя', null=True)
    last_name = models.CharField(max_length=256, verbose_name='Фамилия', null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Мобильный телефон', null=True)
    city = models.CharField(max_length=256, verbose_name='Город проживания', default='Москва')
    info = models.TextField(help_text='Введите основную информацию', null=True)
    profession = models.CharField(max_length=256, verbose_name='Желаемая должность', null=True)
    work_experience = models.BooleanField(default=False, verbose_name='Опыт работы', null=True)
    education = models.CharField(max_length=256, verbose_name='Образование', null=True)
    languages = models.CharField(max_length=256, verbose_name='Владение языками', null=True)

    def __str__(self):
        return '{0} {1}, тел: {2}'.format(self.last_name, self.first_name, self.phone_number)


class Vacancy(models.Model):
    # Модель представляющая вакансии
    employer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=25, verbose_name='Наименование компании', null=True)
    company_cover = models.ImageField(upload_to='images/', default='images/enterprise.png')
    phone_number = models.CharField(max_length=20, verbose_name='Мобильный телефон', null=True)
    info = models.TextField(help_text='Введите основную информацию', null=True)
    profession = models.CharField(max_length=50, verbose_name='Искомая должность', null=True)
    work_experience = models.BooleanField(default=False, verbose_name='Опыт работы', null=True)
    education = models.TextField(null=True, blank=True, verbose_name='Образование')
    languages = models.TextField(null=True, blank=True, verbose_name='Владение языками')

    def __str__(self):
        return '{0}, вакансия на должность: {1}'.format(self.company_name, self.profession)

