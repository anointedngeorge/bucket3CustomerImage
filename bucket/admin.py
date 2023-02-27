from django.contrib import admin
from bucket.models import *
import os
# Register your models here.


@admin.register(Gallery)
class BucketAdmin(admin.ModelAdmin):
    list_display=['name','size','type','url','filename','code']
    list_filter = ['code','type','size','name']

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request) -> bool:
        return False

     
    def response_delete(self, request, obj_display, obj_id):
        g =  self.model.objects.all().filter(id=obj_id)
        print(g)
  
        # os.unlink(f"storage/fb/{g.filename}")
        return super().response_delete(request, obj_display, obj_id)