from django.shortcuts import render
from django.views import generic

from todo.models import Task


class ToDoListView(generic.ListView):
    model = Task
    context_object_name = "todo_list"
    template_name = "todo/todo_list.html"
    paginate_by = 5
