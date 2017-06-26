from django.contrib import admin
from .models import mapmusic
# Register your models here.


@admin.register(mapmusic)
class Mapmusic(admin.ModelAdmin):
    fields=('display','reviewtext',('musicname','lat','lng'),('uploaderemail','uploadtime'),'text','musicfile')
    def get_readonly_fields(self,request,obj=None):
        if not request.user.is_superuser:
            return ['musicname','lat','lng','uploaderemail','uploadtime','text','musicfile']
        return ['musicname','lat','lng','uploaderemail','uploadtime','musicfile']
