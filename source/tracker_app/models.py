from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError


def validate_starts_with_letter(value):
    if value and not value[0].isalpha():
        raise ValidationError('Название задачи должно начинаться с буквы.')


def validate_min_two_words(value):
    if value and len(value.split()) < 2:
        raise ValidationError('Описание должно содержать минимум два слова.')


class Type(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'type'


class Task(models.Model):
    summary = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        validators=[validate_starts_with_letter],
    )
    description = models.TextField(
        null=True,
        blank=True,
        validators=[validate_min_two_words],
    )
    status = models.ForeignKey('Status', on_delete=models.RESTRICT, related_name='tasks', default=1)
    type = models.ManyToManyField(Type, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('Project', on_delete=models.RESTRICT, related_name='tasks')

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

class Project(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ManyToManyField(get_user_model(), related_name='projects', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'