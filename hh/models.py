from django.db import models
import uuid


class Worker(models.Model):
    # Модель представляющая работников
    phone_number = models.CharField(primary_key=True, max_length=20, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    email = models.EmailField(null=True, blank=True, verbose_name='Почта')
    city = models.CharField(max_length=256, verbose_name='Город')

    def __str__(self):
        return '{0} {1} (тел. {2})'.format(self.first_name, self.last_name, self.phone_number)


class Resume(models.Model):
    # Модель представляющая резюме
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    workers_phone = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    info = models.TextField(help_text='Введите основную информацию')
    profession = models.CharField(max_length=256, verbose_name='Желаемая должность')
    work_experience = models.BooleanField(default=False, verbose_name='Опыт работы')
    education = models.CharField(max_length=256, verbose_name='Образование')
    languages = models.CharField(max_length=256, verbose_name='Владение языками')

    def __str__(self):
        return self.profession


class Employer(models.Model):
    # Модель представляющая работодателей
    phone_number = models.CharField(primary_key=True, max_length=20, verbose_name='Номер телефона')
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    email = models.EmailField(null=True, blank=True, verbose_name='Почта')
    company_name = models.CharField(max_length=256, verbose_name='Название компании')
    region = models.CharField(max_length=256, verbose_name='Регион')

    def __str__(self):
        return self.company_name, self.phone_number


class Vacancy(models.Model):
    # Модель представляющая вакансии
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    employers_phone = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True)
    info = models.TextField(help_text='Введите основную информацию')
    profession = models.CharField(max_length=256, verbose_name='Искомая должность')
    work_experience = models.BooleanField(default=False, verbose_name='Требуемый опыт работы')
    education = models.CharField(max_length=256, verbose_name='Образование')
    languages = models.CharField(max_length=256, verbose_name='Владение языками')

    def __str__(self):
        return self.profession, self.employers_phone
