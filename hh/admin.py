from django.contrib import admin
from .models import Employer, Worker, Vacancy, Resume


# Register your models here.
admin.site.register(Employer)
admin.site.register(Worker)
admin.site.register(Vacancy)
admin.site.register(Resume)
