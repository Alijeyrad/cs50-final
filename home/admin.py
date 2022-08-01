from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_posted'
    empty_value_display = '-empty-'
    list_display = ('subject', 'date_posted', 'email', )
    ordering = ['-date_posted']
    search_fields = ['email', 'subject', 'message']
    list_filter = ('is_user',)