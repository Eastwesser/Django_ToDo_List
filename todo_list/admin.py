from django.contrib import admin

from .models import ToDoItem  # Importing ToDoItem model from models.py in the same directory


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "done"
    list_display_links = 'id', 'title'

# admin.site.register(ToDoItem)  # Register ToDoItem model with the admin site
