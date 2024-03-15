from django.contrib import admin

from course.models import Course, Teacher, Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'price', 'start_date', 'end_date']
    search_fields = ['name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
