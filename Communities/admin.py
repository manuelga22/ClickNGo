from django.contrib import admin
from .models import Community

admin.site.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description', 'image']
# Register your models here.
