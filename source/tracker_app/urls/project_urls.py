from django.urls import path, include
from tracker_app.views.projects import CreateProjectView, ProjectListView, DetailProjectView, UpdateProjectView, \
    DeleteProjectView, ProjectUserAddView, RemoveUserFromProjectView, ProjectUserManageView

urlpatterns = [
    path('', ProjectListView.as_view(), name='list_project'),
    path('detail/<int:pk>/', DetailProjectView.as_view(), name='detail_project' ),
    path('project/create/', CreateProjectView.as_view(), name='create_project'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),
    path('project/<int:pk>/add-user/', ProjectUserAddView.as_view(), name='user_add_project'),
    path('project/<int:pk>/remove-user/<int:user_id>/', RemoveUserFromProjectView.as_view(), name='remove_user'),
    path('user/manage/<int:pk>/', ProjectUserManageView.as_view(), name='add_user'),
]