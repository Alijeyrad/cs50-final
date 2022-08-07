from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    empty_value_display = '-empty-'
    list_display = ('username', 'email', 'is_doctor', 'date_joined', )
    ordering = ['-date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'about']
    list_filter = ('is_doctor',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_posted'

admin.site.register(Follow)
admin.site.register(Star)