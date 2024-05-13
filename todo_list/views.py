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


class ToDoListIndexView(TemplateView):
    template_name = "todo_list/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_items"] = ToDoItem.objects.all()
        return context


class ToDoListView(ListView):
    template_name = "todo_list/index.html"
