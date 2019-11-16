from django.contrib import admin
<<<<<<< HEAD
from .models import Community

admin.site.register(Community)
class CommunityAdmin(admin.ModelAdmin):
=======
from .models import Communities

admin.site.register(Communities)
class CommunitiesAdmin(admin.ModelAdmin):
>>>>>>> c4aa71058bef52a9bbb55edfe79bec6239f18f5b
    list_display = ['Name', 'Description', 'image']
# Register your models here.
