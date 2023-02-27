from django.contrib import admin
from bucket.models import *
import os
# Register your models here.


@admin.register(Gallery)
class BucketAdmin(admin.ModelAdmin):
    list_display=['name','size','type','url','filename','code']
    list_filter = ['code','type','size','name']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request) -> bool:
        return False

     