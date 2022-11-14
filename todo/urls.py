from django.urls import path
from .views import TaskView, TagView, TaskCreateView, TaskDeleteView

app_name = "todo"

urlpatterns = [
    path("", TaskView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    path("tags/", TagView.as_view(), name="tag_list"),
]
