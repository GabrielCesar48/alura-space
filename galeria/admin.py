
from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'publicada')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_per_page = 10
    list_editable = ('publicada',)
    
admin.site.register(Fotografia, ListandoFotografias)


