from django.contrib import admin
from .models import Home
from .models import Hblogs
from .models import HImage
from .models import HLogo


@admin.register(Home)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','image','news')

@admin.register(Hblogs)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading','author','blogs')

@admin.register(HImage)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image')


@admin.register(HLogo)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image')


