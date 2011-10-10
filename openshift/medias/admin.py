from medias.models import *
from medias.forms import *
from django.forms import *
from django.contrib import admin


class AlbumMediaInLine(admin.TabularInline):
    model=AlbumMedias
    extra=0

class AlbumAdmin(admin.ModelAdmin):
    form=AlbumForm
    list_display = ('str_name', 'str_description','str_type')
    list_filter = ('str_type',)
    ordering = ('str_type','str_name')
    search_fields = ('str_name','str_description')

    #fields = ('str_type','str_name', 'str_description','str_file','str_url')   
    inlines=[AlbumMediaInLine,]    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        

class MediaAdmin(admin.ModelAdmin):
    
    form=MediasForm
    list_display = ('str_name', 'str_url','str_file','str_type')
    list_filter = ('str_type',)
    ordering = ('str_type','str_name')
    search_fields = ('str_name','str_description','str_url','str_file')

    #fields = ('str_type','str_name', 'str_description','str_file','str_url')       
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        
admin.site.register(Medias,MediaAdmin)
admin.site.register(MediaAlbum,AlbumAdmin)
