from django.contrib import admin
from .models import Communities

admin.site.register(Communities)
class CommunitiesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description', 'image']
# Register your models here.
