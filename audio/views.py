from django.shortcuts import render
from .models import (Audios,GenredAudio,TagedAudio,
	                 MoodedAudio,AudiosCountry,Playlists,AudiosPlaylist,
	                 Podcasts,Episodes,TagedPlaylist,TagedEpisodes)
from django.views.decorators.csrf import csrf_exempt
import logging
from django.http import Http404
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.db.models import F
from meta.models import Tag
import redis
from django.conf import settings
import json
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .AudioSerializer import AudiSerializer
from rest_framework import permissions


# connect to redis
redisClient = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)


@csrf_exempt
def audioByName(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio name"})

			audios = Audios.objects.filter(name__icontains=name).values()
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by name")
			return JsonResponse({'error': "invalid audio name"})
	else:
		return JsonResponse({'error': "invalid audio by name request "})


def audioByLanguage(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio Language"})

			audios = Audios.objects.filter(language__name__icontains=name).values()
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by Language")
			return JsonResponse({'error': "invalid audio Language"})
	else:
		return JsonResponse({'error': "invalid audio by Language request "})


def audioByGenre(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio Genre"})

			audios = GenredAudio.objects.filter(genre__name__icontains=name).values('audios__duration','audios__name',
				'audios__language__name','audios__artist_name','audios__annotation','audios__avatar','audios__audio',
				'audios__streamed','audios__rating','audios__created')
			total = audios.count()
			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by Genre")
			return JsonResponse({'error': "invalid audio Genre"})
	else:
		return JsonResponse({'error': "invalid audio by Genre request "})


def audioByTag(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio Tag"})

			audios = TagedAudio.objects.filter(tag__name__icontains=name).values('audios__pk','audios__duration','audios__name',
				'audios__language__name','audios__artist_name','audios__annotation','audios__avatar','audios__audio',
				'audios__streamed','audios__rating','audios__created')
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by Tag")
			return JsonResponse({'error': "invalid audio Tag"})
	else:
		return JsonResponse({'error': "invalid audio by Tag request "})


def audioByMood(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio Mood"})

			audios = MoodedAudio.objects.filter(moods__name__icontains=name).values('audios__name',
				'audios__language__name','audios__name','audios__annotation','audios__avatar','audios__audio',
				'audios__streamed')
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			audios=json.dumps(audios)
			return JsonResponse(audios,safe=False)
		except:
			logging.exception("Exception occurred at processing audio by Mood")
			return JsonResponse({'error': "Iinvalid audio Mood"})
	else:
		return JsonResponse({'error': "invalid audio by Mood request "})


def audioByCountry(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio country"})

			audios = AudiosCountry.objects.filter(country__name__icontains=name).values('audio__duration','audio__name',
				'audio__language__name','audio__artist_name','audio__annotation','audio__avatar','audio__audio',
				'audio__streamed','audio__rating','audio__created')
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by country")
			return JsonResponse({'error': "invalid audio country"})
	else:
		return JsonResponse({'error': "invalid audio by country request "})


def audioByArtistName(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio artist_name"})

			audios = Audios.objects.filter(artist_name__icontains=name).values()
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by artist_name")
			return JsonResponse({'error': "invalid audio artist_name"})
	else:
		return JsonResponse({'error': "invalid audio by artist_name request "})


def audioByAnnotation(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid audio Annotation"})

			audios = Audios.objects.filter(annotation__icontains=name).values()
			total = audios.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(audios)
			return JsonResponse({'data': audios,'total':total})
		except:
			logging.exception("Exception occurred at processing audio by Annotation")
			return JsonResponse({'error': "invalid audio Annotation"})
	else:
		return JsonResponse({'error': "invalid audio by Annotation request "})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPlaylist(request):
	if request.method == "POST":
		try:
			annotation = 'none'
			if request.POST.get('name') == None:
				return JsonResponse({'error': "invalid playlist name"})
			if request.POST.get('annon') != None and (len(request.POST.get('annon'))  > 1):
				annotation = request.POST.get('annon')

			playlist = Playlists(name=request.POST.get('name'),annotation=annotation,playlist_creator=request.user)
			playlist.save()
			return JsonResponse({'success': "successfully created playlist","id": 'playlist.pk'})
		except:
			logging.exception("Exception occurred at createPlaylist")
			return JsonResponse({'error': "invalid input to createPlaylist"})
	else:
		return JsonResponse({'error': "invalid  request createPlaylist"})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addToPlaylist(request,pid,aid):
	if request.method == "GET":
		try:
			if pid == None or aid == None:
				return JsonResponse({'error': "invalid playlist or audio identification "})
			try:
				playlist = Playlists.objects.get(pk=int(pid))
				track = Audios.objects.get(pk=int(aid))

				audioplaylist = AudiosPlaylist(playlists=playlist,audios=track)
				audioplaylist.save()
				return JsonResponse({'success': "successfully added to playlist"})

			except Exception as ex:
				logging.exception("Exception occurred at adding audio to playlist")
				return JsonResponse({'error': "Error occurred while adding you track to playlist.Please try again."})
		except:
			logging.exception("Exception occurred at createPlaylist")
			return JsonResponse({'error': "invalid input to createPlaylist"})
	else:
		return JsonResponse({'error': "invalid  request createPlaylist"})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPlaylist(request):
	if request.method == "GET":
		try:
			user = request.user
			playlists = Playlists.objects.filter(playlist_creator=user).values('name','stars','streamed','annotation')
			total = playlists.count()

			if total == 0:
				return JsonResponse({'data':'','total':''})
			print(f'playlists --- {playlists}\ntotal --- {total}')
			return JsonResponse({'data': list(playlists),'total':total})
		except:
			logging.exception("Exception occurred while getting playlists.")
			return JsonResponse({'error': "error while fetching playlist.Please try again."})
	else:
		return JsonResponse({'error': "invalid Playlist request."})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSinglePlaylist(request,name):
	if request.method == "GET":
		try:
			playlist = Playlists.objects.get(name=name).values()
			if playlist == None:
				return JsonResponse({'data':'','total':''})
			return JsonResponse({'data': list(playlists)})
		except:
			logging.exception("Exception occurred while getting playlist.")
			return JsonResponse({'error': "error while fetching playlist.Please try again."})
	else:
		return JsonResponse({'error': "invalid Playlist request."})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAudiosPerPlaylist(request,pid):
	if request.method == "GET":
		try:
			if pid is None:
				return JsonResponse({'error': "invalid playlist indentification."})

			playlist = Playlists.objects.get(pk=int(pid))
			audios = AudiosPlaylist.objects.filter(playlists=playlist).values('audios__duration','audios__name',
				'audios__language__name','audios__artist_name','audios__annotation','audios__avatar','audios__audio',
				'audios__streamed','audios__rating','audios__created')
			total = audios.count()
			if total == 0:
				return JsonResponse({'audios':'','total':''})
			return JsonResponse({'audios': list(audios),'total':total})
		except:
			logging.exception("Exception occurred while getting playlists.")
			return JsonResponse({'error': "error while fetching playlist.Please try again."})
	else:
		return JsonResponse({'error': "invalid Playlist request."})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def playAudio(request,aid):
	if request.method == "GET":
		try:
			if aid is None:
				return JsonResponse({'error': "invalid audio indentification."})
			audio = Audios.objects.get(pk=int(aid)).values()
			audio.streamed = F('streamed') + 1

			# calculate rating based on streamed value
			audio.save()
			audio.refresh_from_db()

			audioplaylist = AudiosPlaylist.objects.filter(audios=audio)
			if audioplaylist != None:
				audioplaylist.streamed = F('streamed') + 1
				audioplaylist.save()
				audioplaylist.refresh_from_db()

			# calculate rating 
			likes = audio.likes
			streamed = audio.streamed 

			audio.rating = (likes/streamed) * 5.0
			audio.save() 
			return JsonResponse({'audios': list(audio),})
		except:
			logging.exception("Exception occurred while fetching audio.")
			return JsonResponse({'error': "error fetching audio.Please try again."})
	else:
		return JsonResponse({'error': "invalid fetching audio."})


def saveToPlaylist(pid,aid):
	try:
		playlist = Playlists.objects.get(pk=int(pid))
		track = Audios.objects.get(pk=int(aid))
		audioplaylist = AudiosPlaylist(playlists=playlist,audios=track)
		audioplaylist.save()
		return True
	except Exception as ex:
		logging.exception("Exception occurred while saving to liked playlists.")
		return False


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likeAudio(request,aid):
	if request.method == "GET":
		try:
			if aid is None:
				return JsonResponse({'error': "invalid audio indentification."})
			audio = Audios.objects.get(pk=int(aid))
			audioid = audio.pk
			audio.likes = F('likes') + 1
			audio.save()
			audio.refresh_from_db()

			# check if likes playlist is created
			playistbyname = Q(name__icontains="likes")
			playlistbyuser = Q(playlist_creator=request.user)
			playlist = Playlists.objects.filter(playistbyname & playlistbyuser).first()
			if playlist != None:
				if saveToPlaylist(playlist.pk,audioid):
					return JsonResponse({'success': "success liked"})
				else:
					return JsonResponse({'error': "audio like failed"})
			else:
				# playlist not found create a new 'likes' playlist
				playlist = Playlists.objects.create(name='likes',playlist_creator=request.user)

				if saveToPlaylist(playlist.pk,audioid):
					return JsonResponse({'success': "success liked"})
				else:
					return JsonResponse({'error': "audio like failed"})
		except:
			logging.exception("Exception occurred while liking audio.")
			return JsonResponse({'error': "error occured while liking audio.Please try again."})
	else:
		return JsonResponse({'error': "invalid like audio."})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def addTagToPlaylist(request,pid,name):
	if request.method == "GET":
		try:
			if pid == None or name == None:
				return JsonResponse({'error': "invalid playlist or tag identification "})
			try:
				playlist = Playlists.objects.get(pk=int(pid))

				# get the tag object if not create new one
				tag = Tag.objects.filter(name__icontains=name).first()
				if tag != None:
					# tag exists and check if the playlist occured already
					tagedPlaylistExisis = TagedPlaylist.objects.filter(tag=tag).first()

					if tagedPlaylistExisis == None:
						tagplaylist = TagedPlaylist.objects.create(playlists=playlist,tag=tag)
						return JsonResponse({'success': "successfully added tag to playlist"})
					else:
						return JsonResponse({'error': "playlist with tag name already exists."})
				else:
					tag = Tag.objects.create(name=name)
					tagplaylist = TagedPlaylist.objects.create(playlists=playlist,tag=tag)
			except Exception as ex:
				logging.exception("Exception occurred at adding tag to playlist")
				return JsonResponse({'error': "Error occurred while adding tag to playlist.Please try again."})
		except:
			logging.exception("Exception occurred at createPlaylist")
			return JsonResponse({'error': "invalid input to add tag to playlist"})
	else:
		return JsonResponse({'error': "invalid  request to add tag to playlist"})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def playlistByName(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid playlist name"})

			playlists = Playlists.objects.filter(name__icontains=name).values()
			total = playlists.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			playlists = list(playlists)
			return JsonResponse({'data': playlists,'total':total})
		except:
			logging.exception("Exception occurred at processing playlist name")
			return JsonResponse({'error': "invalid playlist name"})
	else:
		return JsonResponse({'error': "invalid playlist name request "})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def playlistByTag(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid playlist tag"})

			playlists = TagedPlaylist.objects.filter(tag__name__icontains=name).values()
			total = playlists.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			playlists = list(playlists)
			return JsonResponse({'data': playlists,'total':total})
		except:
			logging.exception("Exception occurred at processing playlist tag")
			return JsonResponse({'error': "invalid playlist tag"})
	else:
		return JsonResponse({'error': "invalid playlist tag request "})


def PodcastByName(request,name):
	if request.method == "GET":
		try:	
			if len(name) == 0:
				return JsonResponse({'error': "invalid podcast name"})
			podcasts = Podcasts.objects.filter(name__icontains=name).values('name','language__name','podcast_creator','annotation','avatar','rating','created')
			total = podcasts.count()

			podcasts = list(podcasts)

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			audios = list(podcasts)
			return JsonResponse({'data': podcasts,'total':total})
		except:
			logging.exception("Exception occurred at processing podcast by name ")
			return JsonResponse({'error': "invalid audio podacast name"})
	else:
		return JsonResponse({'error': "invalid podcast by name request "})


def singlePodcastByName(request,pid):
	if request.method == "GET":
		try:
			if pid is None:
				return JsonResponse({'error': "invalid podcast name"})
			podcasts = Podcasts.objects.values_list('name','language__name','podcast_creator','annotation','avatar','rating','created').get(pk=int(pid))
			if podcasts == None:
				return JsonResponse({'data': ''})
			podcasts = list(podcasts)
			return JsonResponse({'data': podcasts})
		except:
			logging.exception("Exception occurred at processing podcast by id ")
			return JsonResponse({'error': "invalid audio podacast id"})
	else:
		return JsonResponse({'error': "invalid podcast by id request "})


# redis cached view 
def PodcastBylangauge(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid podcast Language"})

			# check if redis server is running
			if redisClient:
				if redisClient.exists("search:podcasts"):
            		# check if the search key for podcasts is set
					print('**********  CACHE FOUND **********')
					result = redisClient.hget("search:podcasts",name);
					if result:
						data = redisClient.hget("search:podcasts",name).decode('utf8').replace("'",'"')	
						data = json.dumps(data)
						total = redisClient.hget("search:podcasts",f"{name}:total").decode('utf8').replace("'",'"')	
						total = json.dumps(total)
						print(f"--- Data : {data} \n--- Total {total}")	
				else:
					print('***********  CACHE NOT FOUND  ***********')
					podcasts = Podcasts.objects.filter(language__name__icontains=name).values('name','language__name','podcast_creator','annotation','avatar','rating','created')
					total = podcasts.count()
					if total == 0:
						return JsonResponse({'data': '','total': ''})

					data = list(podcasts)

					# cache the results
					print(f'-- caching result --')
					redisClient.hset("search:podcasts", f"{name}", str(data))
					redisClient.hset("search:podcasts",f"{name}:total",str(total))

					print('-- output cached results -- -- -- ')
					key = f'search:podcasts'
					print(f'{redisClient.hget(key, name)}')

			#podcasts = list(podcasts)
			return JsonResponse({'data': data,'total':total})
		except:
			logging.exception("Exception occurred at processing podcast by Language ")
			return JsonResponse({'error': "invalid audio podacast Language"})
	else:
		return JsonResponse({'error': "invalid podcast by Language request "})


def PodcastByCreator(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid podcast creator"})
			podcasts = Podcasts.objects.filter(podcast_creator__icontains=name).values('name','language__name','podcast_creator','annotation','avatar','rating','created')
			total = podcasts.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			podcasts = list(podcasts)
			return JsonResponse({'data': podcasts,'total':total})
		except:
			logging.exception("Exception occurred at processing podcast by creator ")
			return JsonResponse({'error': "invalid audio podacast creator"})
	else:
		return JsonResponse({'error': "invalid podcast by creator request "})


def episodesPerPodcast(request,pid):
	if request.method == "GET":
		try:
			if int(pid) == 0:
				return JsonResponse({'error': "invalid epiosdes per podcast"})
			podcasts = Episodes.objects.filter(podcasts__pk=pid).values()
			total = podcasts.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			podcasts = list(podcasts)
			return JsonResponse({'data': podcasts,'total':total})
		except:
			logging.exception("Exception occurred at processing epiosdes per podcast")
			return JsonResponse({'error': "invalid epiosdes per podcast"})
	else:
		return JsonResponse({'error': "invalid epiosdes per podcast"})


def getSingleEpisode(request,pid):
	if request.method == "GET":
		try:
			if int(pid) == 0:
				return JsonResponse({'error': "invalid epiosdes id"})
			episode = Episodes.objects.get(pk=pid)
			episode.streamed = F('streamed') + 1
			episode.save()
			episode.refresh_from_db()

			episode = Episodes.objects.values_list('name','audios__pk','audios__name','tag__name','podcasts__name','annotation','likes','streamed').get(pk=pid)
			if episode == None:
				return JsonResponse({'data': ''})

			episode = list(episode)
			return JsonResponse({'data': episode})
		except:
			logging.exception("Exception occurred at processing episodes epiosdes id ")
			return JsonResponse({'error': "invalid episodes id"})
	else:
		return JsonResponse({'error': "invalid episodes id"})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def episodesByTag(request,name):
	if request.method == "GET":
		try:
			if len(name) == 0:
				return JsonResponse({'error': "invalid episodes tag"})

			episodes = TagedEpisodes.objects.filter(tag__name__icontains=name).values('tag__name','episodes__name','episodes__audios__name','episodes__podcasts__name',
				                     'episodes__podcasts__annotation','episodes__podcasts__likes')
			total = episodes.count()

			if total == 0:
				return JsonResponse({'data': '','total': ''})

			episodes = list(episodes)
			return JsonResponse({'data': episodes,'total':total})
		except:
			logging.exception("Exception occurred at processing episodes tag")
			return JsonResponse({'error': "invalid episodes tag"})
	else:
		return JsonResponse({'error': "invalid episodes tag request "})


# DRF

class AudioUpload(APIView):
	parser_classes = [MultiPartParser, 	]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request,format=None):
		print(request.data)
		print("\n\n")
		serializer = AudiSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AudioDetail(APIView):

	def get_object(self,pk):
		try:
			return Audios.objects.get(pk=pk)
		except Audios.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		audio = self.get_object(pk)
		serializer = AudiSerializer(audio)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		audio = self.get_object(pk)
		serializer = AudiSerializer(audio, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		audio = self.get_object(pk)
		audio.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

