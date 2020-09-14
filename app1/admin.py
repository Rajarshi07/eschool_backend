from django.contrib import admin
from .models import course, teacher_form, intern_form
# Register your models here.

admin.site.register(course)
admin.site.register(teacher_form)
admin.site.register(intern_form)

