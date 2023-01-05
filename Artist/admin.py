from django.contrib import admin
from .models import (Artist,Links,Subscribers,Action,UserFollowing)
from django.urls import reverse
from django.utils.html import format_html


class ArtistLinksAdminInline(admin.TabularInline):
    model = Links
    extra = 2

class ArtistAdmin(admin.ModelAdmin):
    inlines = [ArtistLinksAdminInline]
    list_display = ('id','user_acc','biography','artist_name','country')


class LinksAdmin(admin.ModelAdmin):
    list_display=('id','zArtist','link','link_description','link_2_artist','artistName')

    def link_2_artist(self,obj):
        link = reverse("admin:Artist_links_change",args=[obj.zArtist.id])
        return format_html(u'<a href="%s">%s</a>' % (link,obj.zArtist.artist_name))
    link_2_artist.allow_tags = True

    @admin.display(description='artist name')
    def artistName(self,obj):
        return obj.zArtist.artist_name


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Links, LinksAdmin)