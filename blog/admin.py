from django.contrib import admin

from.models import Post
from.models import extenduser

@admin.register(Post)

class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
    
admin.site.register(extenduser)

