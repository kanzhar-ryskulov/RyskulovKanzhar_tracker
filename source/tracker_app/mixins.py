from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from tracker_app.models import Project


class ManagerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Project Manager').exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ManagerOrLeadRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name__in=['Project Manager', 'Team Lead']).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class InProjectMixin:
    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        if not project.user.filter(pk=request.user.pk).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)