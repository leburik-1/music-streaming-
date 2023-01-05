from django.contrib import admin
from .models import Country,Language,Genre,Tag,Moods


admin.site.site_header  =  "Nusah Audio"
admin.site.site_title  =  "Nusah Meta"
admin.site.index_title  =  "Nusah Audio Meta Adminstration"


class CountryAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    search_fields = ['name']

class LanguageAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    search_fields = ['name']

class GenreAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display=('id','name',)
    search_fields = ['name']

class MoodsAdmin(admin.ModelAdmin):
    list_display=('id','name',"avatar")
    search_fields = ['name']


admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Moods, MoodsAdmin)




