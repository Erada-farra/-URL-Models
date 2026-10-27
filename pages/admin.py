
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'university_id', 'age', 'salary')
    search_fields = ('full_name', 'university_id')