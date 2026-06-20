from django.urls import path, include
from tracker_app.views.projects import CreateProjectView, ProjectListView, DetailProjectView

urlpatterns = [
    path('', ProjectListView.as_view(), name='list_project'),
    path('detail/<int:pk>/', DetailProjectView.as_view(), name='detail_project' ),
    path('project/create/', CreateProjectView.as_view(), name='create_project'),
]