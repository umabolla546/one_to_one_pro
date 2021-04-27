from django.contrib import admin
from .models import student,cource
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','location','age']

class courceAdmin(admin.ModelAdmin):
    list_display = ['id','cname','fee']

admin.site.register(student,studentAdmin)
admin.site.register(cource,courceAdmin)