from django.contrib import admin

# Register your models here.

from .models import Mblock
from .models import Note

admin.site.register(Mblock)
admin.site.register(Note)