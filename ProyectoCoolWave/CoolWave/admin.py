from django.contrib import admin
from .models import SliderIndex,MisionVision,Insumos,Imggal

# Register your models here.
class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields = ['nombre','descripcion']
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['id','imgtitle']
    search_fields = ['id','imgtitle']
    list_per_page = 10

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(MisionVision)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(Imggal, GaleriaAdmin)