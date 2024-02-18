from django.contrib import admin
from .models import query
class tab(admin.ModelAdmin):
    list_display=['name','fathername','email','contact','subject','message']
admin.site.register(query,tab)   
# Register your models here. 
