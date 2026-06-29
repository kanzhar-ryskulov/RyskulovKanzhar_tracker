from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from tracker_app.forms import SearchForm, ProjectForm
from tracker_app.mixins import ManagerOrLeadRequiredMixin, ManagerRequiredMixin, InProjectMixin
from tracker_app.models import Project

User = get_user_model()
class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1

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

        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class DetailProjectView(DetailView):
    template_name = 'project/detail_project.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['all_users'] = User.objects.exclude(id__in=self.object.user.all())
        return context



class CreateProjectView(LoginRequiredMixin, ManagerRequiredMixin,CreateView):
    template_name = 'project/create_project.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('list_project')


    def form_valid(self, form):
        project = form.save()
        project.user.add(self.request.user)
        return redirect('list_project')

class UpdateProjectView(LoginRequiredMixin, ManagerRequiredMixin , InProjectMixin, UpdateView):
    template_name = 'project/update_project.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('list_project')


class DeleteProjectView(LoginRequiredMixin, ManagerRequiredMixin, InProjectMixin , DeleteView):
    template_name = 'project/delete_project.html'
    model = Project
    success_url = reverse_lazy('list_project')

class ProjectUserManageView(LoginRequiredMixin, ManagerOrLeadRequiredMixin, InProjectMixin, DetailView):
    template_name = 'project/add_user.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['all_users'] = User.objects.exclude(id__in=self.object.user.all())
        return context


class ProjectUserAddView(LoginRequiredMixin, ManagerOrLeadRequiredMixin, InProjectMixin, View):

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        user = get_object_or_404(User, pk=request.POST["user_id"])
        project.user.add(user)

        return redirect("detail_project", pk=project.pk)


class RemoveUserFromProjectView(LoginRequiredMixin, ManagerOrLeadRequiredMixin, InProjectMixin,View):

    def post(self, request, pk, user_id):
        project = get_object_or_404(Project, pk=pk)
        user = get_object_or_404(User, id=user_id)

        project.user.remove(user)
        return redirect('detail_project', pk=pk)

