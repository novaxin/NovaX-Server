from django.contrib import admin
from .models import Note,Command,LikeOrDislike
# Register your models here.

admin.site.register(Note)
admin.site.register(Command)
admin.site.register(LikeOrDislike)
