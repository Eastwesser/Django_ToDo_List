from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="todo_list/index.html")
