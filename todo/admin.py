from django.contrib import admin

from .models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "complete"]
    list_filter = ["name", "date"]

