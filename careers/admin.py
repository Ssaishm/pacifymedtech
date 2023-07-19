from django.contrib import admin
from .models import Careers


@admin.register(Careers)
class careersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','details','location')
