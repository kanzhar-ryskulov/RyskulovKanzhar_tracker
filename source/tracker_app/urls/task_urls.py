from django.urls import path
from tracker_app.views import DetailTaskView, CreateTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('task/<int:pk>/detail/', DetailTaskView.as_view(), name='detail'),
    path('project/<int:pk>/task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]