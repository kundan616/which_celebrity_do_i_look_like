from django.contrib import admin
from .models import tutorial
# Register your models here.



class tutadmin(admin.ModelAdmin):
    fieldsets=[("date/title",{"fields":["title","published","desc"]})
]    
admin.site.register(tutorial,tutadmin)
