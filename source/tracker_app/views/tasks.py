from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import TemplateView, View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from tracker_app.models import Task, Project
from tracker_app.forms import TaskForm, SearchForm


class MainView(ListView):
    template_name = 'task/main_page.html'
    context_object_name = 'task'
    model = Task
    paginate_by = 5
    paginate_orphans = 1
    queryset = Task.objects.all()

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            search = self.form.cleaned_data['search']
        return search

    def get_queryset(self):
        queryset = super().get_queryset()

        if queryset.exists():
            queryset = queryset.filter(Q(project__title__icontains=self.search_value) | Q(project__description__icontains=self.search_value))
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['search_form'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

        return context



class DetailTaskView(DetailView):
    template_name = 'task/task.html'
    context_object_name = 'task'
    model = Task


class CreateTaskView(CreateView):
    template_name = "task/add_task.html"
    form_class = TaskForm
    success_url = reverse_lazy('main')



class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('main')


class DeleteTaskView(DeleteView):
    template_name = 'task/delete_task.html'
    model = Task
    success_url = reverse_lazy('main')




