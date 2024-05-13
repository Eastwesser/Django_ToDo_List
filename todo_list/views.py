from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import ToDoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()[:4]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.order_by("id").all()[:4]  # можно ставить ограничения


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneIndexView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem
