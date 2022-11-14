from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tag


class TaskView(generic.ListView):
    model = Task
    paginate_by = 5


class TagView(generic.ListView):
    model = Tag
    paginate_by = 5

