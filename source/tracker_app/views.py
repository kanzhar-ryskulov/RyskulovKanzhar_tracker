from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View

from tracker_app.models import Task
from tracker_app.forms import TaskForm


class MainView(TemplateView):
    template_name = 'task/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context


class DetailTaskView(TemplateView):
    template_name = 'task/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        context['task'] = task
        return context


class CreateTaskView(View):
    form = TaskForm()

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/add_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

        return render(request, 'task/add_task.html', {'form': form})


class UpdateTaskView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        form = TaskForm(instance=task)
        return render(request, 'task/update_task.html', {'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect('main')
        return render(request, 'task/update_task.html', {'form': form, 'task': task})


class DeleteTaskView(View):
    def get(self, request, *args, **kwargs, ):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return render(request, "task/delete_task.html", {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task.delete()
        return redirect('main')



