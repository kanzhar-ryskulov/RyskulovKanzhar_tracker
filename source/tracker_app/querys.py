from datetime import timedelta
from django.utils import timezone
from django.db.models import Q

from models import Task

one_month_ago = timezone.now() - timedelta(days=30)

# Запрос 1
query1 = Task.objects.filter(
    status__title='Закрыта',
    updated_at__gte=one_month_ago,
)

for task in query1:
    print(f" [{task.pk}] {task.summary} | {task.status.title}")

# Запрос 2

query2 = Task.objects.filter(
    Q(status__title='Открыта') | Q(status__title='В работе'),
    Q(type__title='Баг') | Q(type__title='Документация'),
).distinct()

for task in query2:
    types = ', '.join(task.type.values_list('title', flat=True))
    print(f"  [{task.pk}] {task.summary} | типы: {types} | статус: {task.status.title}")

# Запрос 3

query3 = Task.objects.filter(
    ~Q(status__title='Закрыта'),
).filter(
    Q(summary__icontains='bug') | Q(type__title='Баг')
).distinct()

for task in query3:
    types = ', '.join(task.type.values_list('title', flat=True))
    print(f"  [{task.pk}] {task.summary} | типы: {types} | статус: {task.status.title}")

# bonus 1

bonus1 = Task.objects.filter(
    ~Q(status__title='Закрыта'),
    Q(summary__icontains='bug') | Q(type__title='Баг')
).distinct().values('id', 'summary', 'type__title', 'status__title')

for row in bonus1:
    print(row)
