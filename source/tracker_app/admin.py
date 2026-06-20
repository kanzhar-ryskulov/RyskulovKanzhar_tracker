from django.contrib import admin
from tracker_app.models import Type, Status, Task, Project


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'type',)
    ordering = ('-created_at',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date',)
    ordering = ('-start_date',)
