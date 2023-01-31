from django.contrib import admin
from . import models

@admin.register(models.Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'register_date', 'is_connected')