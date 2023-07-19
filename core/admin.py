from django.contrib import admin
from .models import wContact


@admin.register(wContact)
class wContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','number','organization','description', 'email')