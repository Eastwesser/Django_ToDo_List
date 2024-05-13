from django.urls import path

from . import views

app_name = "todo_list"

urlpatterns = [
    path("", views.ToDoListView.as_view(), name="index"),
]
