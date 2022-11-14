from django.urls import path
from .views import TaskView, TagView, TaskCreateView, TaskDeleteView, TagCreateView, TagDeleteView

app_name = "todo"

urlpatterns = [
    path("", TaskView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    path("tag/", TagView.as_view(), name="tag_list"),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
