from django.db import models
from account.models import User
from meta.models import Country,Language,Genre,Tag,Moods
from utils import saveAudioImage,saveAudioFile,savePodcastImage,savePodcastAudio
from django.core.validators import FileExtensionValidator
from Artist.models import Artist

class Audios(models.Model):
	name = models.CharField(max_length = 29,blank=True,null=True)
	duration = models.DecimalField(default=0.0,max_digits=5, decimal_places=2)
	language = models.ForeignKey(Language,on_delete=models.PROTECT,related_name='audios')
	zartist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='myaudios')
	annotation = models.CharField(max_length=50)
	avatar = models.ImageField(upload_to=saveAudioImage, 
    	      validators=[FileExtensionValidator(allowed_extensions=["jpg","png","jpeg"])], null=True, blank=True)
	audio = models.FileField(upload_to=saveAudioFile, 
    	     validators=[FileExtensionValidator(allowed_extensions=["mp3","acc"])], null=True, blank=True)
	streamed = models.PositiveIntegerField(default=0)
	rating = models.DecimalField(default=0.0,max_digits=2, decimal_places=1)
	created = models.DateTimeField(auto_now_add=True)
	likes = models.PositiveIntegerField(default=0)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class GenredAudio(models.Model):
	genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='gaudios')
	audios = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='agenres')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.genre.name} - {self.audios.name}' 


class TagedAudio(models.Model):
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='taudios')
	audios = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='atags')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.tag.name} - {self.audios.name}' 

class MoodedAudio(models.Model):
	moods = models.ForeignKey(Moods,on_delete=models.CASCADE,related_name='maudios')
	audios = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='amoods')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.moods.name} - {self.audios.name}' 


class AudiosCountry(models.Model):
	audio = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='acountry')
	country = models.ForeignKey(Country,on_delete=models.PROTECT,related_name='caudio')
	
	def __str__(self):
		return f'{self.country.name} - {self.audio.name}' 



class Playlists(models.Model):
	name = models.CharField(max_length = 29,blank=True,null=True)
	playlist_creator = models.ForeignKey(User,on_delete=models.PROTECT,related_name='playlist')
	stars = models.DecimalField(default=0.0,max_digits=2, decimal_places=1)
	streamed = models.PositiveIntegerField(default=0)
	annotation = models.CharField(max_length=50,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f'{self.name}' 


class TagedPlaylist(models.Model):
	playlists = models.ForeignKey(Playlists,on_delete=models.PROTECT,related_name='tagedplaylst')
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='tagedplaylists')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):	
		return f'{self.tag.name} - {self.playlists.name}' 


class AudiosPlaylist(models.Model):
	playlists = models.ForeignKey(Playlists,on_delete=models.PROTECT,related_name='audiosplaylist')
	audios = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='playlistaudio')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f'{self.playlists.name} - {self.audios.name}'


class Podcasts(models.Model):
    name = models.CharField(max_length = 29,blank=True,null=True)
    language = models.ForeignKey(Language,on_delete=models.PROTECT,related_name='podcastslang')
    creator = models.ForeignKey(User,on_delete=models.PROTECT,related_name='podcastsuser')
    podcast_creator = models.CharField(max_length = 29,blank=True,null=True)
    annotation = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=savePodcastImage, 
    	      validators=[FileExtensionValidator(allowed_extensions=["jpg","png","jpeg"])], null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(default=0.0,max_digits=2, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.name


class TagedPodcast(models.Model):
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='tagedpodcast')
	podcast = models.ForeignKey(Podcasts,on_delete=models.CASCADE,related_name='podcaststaged')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.tag.name} - {self.podcast.name}' 


class Episodes(models.Model):
    name = models.CharField(max_length = 29,blank=True,null=True)
    audios = models.ForeignKey(Audios,on_delete=models.CASCADE,related_name='episodesaudio')
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='episodetags')
    podcasts = models.ForeignKey(Podcasts,on_delete=models.CASCADE,related_name='podcastepisodes')
    annotation = models.CharField(max_length=255,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    streamed = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.name


class TagedEpisodes(models.Model):
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='tagedepisodes')
	episodes = models.ForeignKey(Episodes,on_delete=models.CASCADE,related_name='episodestag')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.tag.name} - {self.episodes.name}'


class Subscriptions(models.Model):
    podcasts = models.ForeignKey(Podcasts,on_delete=models.CASCADE,related_name='subscribedusers')
    subscriber = models.ForeignKey(User,on_delete=models.PROTECT,related_name='podcastsubscription')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
    	return self.name

