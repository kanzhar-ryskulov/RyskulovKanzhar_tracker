from django.contrib import admin
from tracker_app.models import Type, Status, Task


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description', 'status', 'type', 'created_at', 'updated_at')
    list_filter = ('status', 'type',)
    ordering = ('-created_at',)