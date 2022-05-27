from django.contrib import admin
from .models import Color_Code_Data
# Register your models here.

class Color_Code_admin(admin.ModelAdmin):
    list_display = ['color_tag']

admin.site.register(Color_Code_Data, Color_Code_admin)