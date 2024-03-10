from django.contrib import admin
from listapp.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=('detail','uid','iscompleted')
    list_filter=('uid',)

admin.site.register(Todo,TodoAdmin)