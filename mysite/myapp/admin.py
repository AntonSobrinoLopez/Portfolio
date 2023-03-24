from django.contrib import admin
from .models import Test

class TestAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Test,TestAdmin)