from django.forms import ModelForm
from .models import Resume, Vacancy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ('worker',)


class CreateVacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ('employer',)
