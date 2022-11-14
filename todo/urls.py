from django.urls import path
from .views import ToDoListView

app_name = "todo"

urlpatterns = [
    path("", ToDoListView.as_view(), name="todo_list"),

    ]