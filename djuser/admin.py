from django.contrib import admin
from .models import DJuser


class DJuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(DJuser, DJuserAdmin)
