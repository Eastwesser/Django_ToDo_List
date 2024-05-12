from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = [
        "Item 1",
        "item 2",
        "Item 3",
        "Item 4",
    ]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )
