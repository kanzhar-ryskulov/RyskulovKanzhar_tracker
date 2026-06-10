from django.db import models

# Create your models here.


class Task(models.Model):
    summary = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.RESTRICT, related_name='tasks')
    type = models.ForeignKey('Type', on_delete=models.RESTRICT, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'task'
        ordering = ['-created_at']

    def __str__(self):
        return self.summary[:20]


class Status(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'status'

class Type(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'type'
