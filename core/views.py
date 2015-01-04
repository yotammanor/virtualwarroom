from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from core.models import Task, TaskEvent, Category

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class HomePageView(TemplateView):
    template_name = 'core/base.html'


class TaskView(DetailView):
    model = Task
    template_name = 'core/task.html'