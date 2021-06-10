from django.contrib import admin

# Register your models here.
from .models import student
from .models import person

admin.site.register(student)
admin.site.register(person)

