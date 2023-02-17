from django.contrib import admin
from to_do_list.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'date_to_do')
    list_filter = ('title', 'date_to_do')
    fields = ('title', 'description', 'status', 'date_to_do')

admin.site.register(Task, TaskAdmin)
