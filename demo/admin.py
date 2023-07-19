from django.contrib import admin
from .models import DemoContact


@admin.register(DemoContact)
class DemoContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','number','organization','description', 'email')
