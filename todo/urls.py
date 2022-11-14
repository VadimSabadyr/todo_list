from django.urls import path
from .views import TaskView, TagView

app_name = "todo"

urlpatterns = [
    path("", TaskView.as_view(), name="task_list"),
    path("tags/", TagView.as_view(), name="tag_list"),
]
