from django.contrib import admin
from django.urls import path
from .views import (audioByName,audioByLanguage,
	                audioByGenre,audioByTag,audioByMood,
	                audioByCountry,audioByArtistName,audioByAnnotation,createPlaylist,
                    addToPlaylist,getPlaylist,getAudiosPerPlaylist,playAudio,likeAudio,
                    playlistByName,playlistByTag,addTagToPlaylist,PodcastByName,singlePodcastByName,
                    PodcastBylangauge,PodcastByCreator,episodesPerPodcast,episodesByTag,getSingleEpisode,
                    AudioUpload,AudioDetail)


urlpatterns = [
    path('name/<str:name>/', audioByName, name='audiobyname'),
    path('lang/<str:name>/', audioByLanguage, name='audioByLanguage'),
    path('genre/<str:name>/', audioByGenre, name='audioByGenre'),
    path('tag/<str:name>/', audioByTag, name='audioByTag'),
    path('mood/<str:name>/', audioByMood, name='audioByMood'),
    path('country/<str:name>/', audioByCountry, name='audioByCountry'),
    path('artist/<str:name>/', audioByArtistName, name='audioByArtistName'),
    path('annon/<str:name>/', audioByAnnotation, name='audioByAnnotation'),

    path('playlist/create/', createPlaylist, name='createPlaylist'),
    path('playlist/audio/add/<int:pid>/<int:aid>/', addToPlaylist, name='addToPlaylist'),
    path('playlist/', getPlaylist, name='getPlaylist'),
    path('playlist/audios/<int:pid>/', getAudiosPerPlaylist, name='getAudiosPerPlaylist'),
    path('play/<int:aid>/', playAudio, name='playAudio'),
    path('like/<int:aid>/', likeAudio, name='likeAudio'),
    path('playlist/name/<str:name>/', playlistByName, name='playlistByName'),
    path('playlist/tag/<str:name>/', playlistByTag, name='playlistByTag'),
    path('playlist/addtag/<int:pid>/<str:name>/', addTagToPlaylist, name='addTagToPlaylist'),

    path('podcast/name/<str:name>/', PodcastByName, name='PodcastByName'),
    path('podcast/namei/<int:pid>/', singlePodcastByName, name='singlePodcastByName'),
    path('podcast/lang/<str:name>/', PodcastBylangauge, name='PodcastBylangauge'),
    path('podcast/creator/<str:name>/', PodcastByCreator, name='PodcastByCreator'),
    path('podcast/episodes/<int:pid>/', episodesPerPodcast, name='episodesPerPodcast'),
    path('podcast/episode/<int:pid>/', getSingleEpisode, name='episodesPerPodcast'),
    path('podcast/episodes/tag/<str:name>/', episodesByTag, name='episodesByTag'),

    #endpoints using django rest framework
    path('upload/',AudioUpload.as_view()),
    path('detail/<int:pk>/',AudioDetail.as_view()),
]
