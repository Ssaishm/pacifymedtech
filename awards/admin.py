from django.contrib import admin
from .models import AImage
from .models import Awards


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','details')


@admin.register(AImage)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image')



