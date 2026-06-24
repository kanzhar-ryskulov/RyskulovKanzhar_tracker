from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from tracker_app.models import Task, Project
from tracker_app.forms import TaskForm


class DetailTaskView(DetailView):
    template_name = 'task/task.html'
    context_object_name = 'task'
    model = Task


class CreateTaskView(LoginRequiredMixin,CreateView):
    template_name = "task/add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy('list_project')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs["pk"])
        form.instance.project = project
        return super().form_valid(form)


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('main')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)


class DeleteTaskView(DeleteView):
    template_name = 'task/delete_task.html'
    model = Task
    success_url = reverse_lazy('main')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        return super().dispatch(request, *args, **kwargs)
