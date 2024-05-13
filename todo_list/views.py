from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)

from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    model = ToDoItem


class ToDoListView(ListView):
    model = ToDoItem
