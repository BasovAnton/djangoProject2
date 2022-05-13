from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

    # # # Поля в списке
    # list_display = ('title', 'public', 'date_add', 'author', 'id', )
    # # # Группировка поля в режиме редактирования
    # fields = ('date_add', ('title', 'public'), 'message', 'author')
    # # # Поля только для чтения в режиме редактирования
    # readonly_fields = ('date_add', )
