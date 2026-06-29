from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from tracker_app.mixins import ManagerOrLeadRequiredMixin, InProjectMixin

from tracker_app.models import Task, Project
from tracker_app.forms import TaskForm


class DetailTaskView(DetailView):
    template_name = 'task/task.html'
    context_object_name = 'task'
    model = Task


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = "task/add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy('detail_project')

    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        if not project.user.filter(pk=request.user.pk).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        project_detail = get_object_or_404(Project, pk=self.kwargs["pk"])
        return reverse('detail_project', kwargs={'pk': project_detail.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs["pk"])
        form.instance.project = project
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if not task.project.user.filter(pk=request.user.pk).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.project.pk})


class DeleteTaskView(LoginRequiredMixin,ManagerOrLeadRequiredMixin, DeleteView):
    template_name = 'task/delete_task.html'
    model = Task
    success_url = reverse_lazy('list_project')

    def dispatch(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if not task.project.user.filter(pk=request.user.pk).exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.project.pk})
