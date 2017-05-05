from django.contrib import admin
from .models import mapmusic
# Register your models here.


@admin.register(mapmusic)
class Mapmusic(admin.ModelAdmin):
    fields=('display','reviewtext',('musicid','lat','lng'),('uploaderemail','uploadtime'),'text')
    def get_readonly_fields(self,request,obj=None):
        if not request.user.is_superuser:
            return ['musicid','lat','lng','uploaderemail','uploadtime','text']
        # return self.readonly_fields
