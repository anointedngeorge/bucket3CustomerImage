from django.contrib import admin
from bucket.models import *
import os
# Register your models here.


@admin.register(Gallery)
class BucketAdmin(admin.ModelAdmin):
    list_display=['name','size','type','url','filename']

    # def has_add_permission(self, request) -> bool:
    #     return False

    # def response_action(self, request, queryset):
    #     print(request)
    #     print('Hy')
    #     return super().response_action(request, queryset)