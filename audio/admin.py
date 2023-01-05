from django.contrib import admin
from .models import (Audios,GenredAudio,TagedAudio,
	                 MoodedAudio,AudiosCountry,Playlists,
	                 AudiosPlaylist,Podcasts,Episodes,TagedPlaylist,
                     Subscriptions,TagedPodcast,TagedEpisodes)

admin.site.site_header  =  "Nusah Audio"
admin.site.site_title  =  "Nusah Audio Process"
admin.site.index_title  =  "Nusah Audio Processing Adminstration"


class AudiosAdmin(admin.ModelAdmin):
    list_display=('id','name','duration','language',
                  'annotation','avatar','audio','streamed','rating','likes')
    search_fields = ['name','annotation','rating']

class GenredAudioAdmin(admin.ModelAdmin):
    list_display=('id','genre','audios',)

class TagedAudioAdmin(admin.ModelAdmin):
    list_display=('id','tag','audios')

class MoodedAudioAdmin(admin.ModelAdmin):
    list_display=('id','moods','audios')

class AudiosCountryAdmin(admin.ModelAdmin):
    list_display=('id','audio',"country")

class TagedPlaylistAdmin(admin.ModelAdmin):
    list_display=('id','playlists',"tag")

class TagedPodCastAdmin(admin.ModelAdmin):
    list_display=('id','tag',"podcast")

class PlaylistsAdmin(admin.ModelAdmin):
    list_display=('id','name','playlist_creator','stars','streamed','annotation')
    search_fields = ['name','annotation','stars']


class EpisodeAdminInline(admin.TabularInline):
    model = Episodes
    extra = 2


class PodcastsAdmin(admin.ModelAdmin):
    inlines = [EpisodeAdminInline]
    list_display=('id','name','language','creator','annotation','avatar','rating')
    search_fields = ['name','language','rating']


class AudiosPlaylistAdmin(admin.ModelAdmin):
    list_display=('id','playlists','audios',)


class TagedEpisodesAdmin(admin.ModelAdmin):
    list_display=('id','tag','episodes',)

class EpisodesAdmin(admin.ModelAdmin):
    list_display=('id','name','audios','tag','podcasts','annotation','likes','streamed')

class SubscriptionsAdmin(admin.ModelAdmin):
    list_display=('id','name','audios','tag','podcasts','annotation',)




admin.site.register(Audios, AudiosAdmin)
admin.site.register(GenredAudio, GenredAudioAdmin)
admin.site.register(TagedAudio, TagedAudioAdmin)
admin.site.register(MoodedAudio, MoodedAudioAdmin)
admin.site.register(AudiosCountry, AudiosCountryAdmin)

admin.site.register(Playlists, PlaylistsAdmin)
admin.site.register(Podcasts, PodcastsAdmin)
admin.site.register(TagedPlaylist, TagedPlaylistAdmin)
admin.site.register(TagedPodcast, TagedPodCastAdmin)
admin.site.register(TagedEpisodes, TagedEpisodesAdmin)
admin.site.register(AudiosPlaylist, AudiosPlaylistAdmin)
admin.site.register(Episodes, EpisodesAdmin)
# admin.site.register(playlistByTag, playlistByTagAdmin)





