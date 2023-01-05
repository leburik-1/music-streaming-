import uuid
import os
from django.core.exceptions import ValidationError


def saveUserImage(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"user/avatar/{myfilename}"

def saveAudioImage(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"audio/avatar/{myfilename}"

def saveAudioFile(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"audio/file/{myfilename}"

def saveMoodImage(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"mood_image/{myfilename}"

def savePodcastImage(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"podcast/avatar/{myfilename}"

def savePodcastAudio(self,filename):
	ext = filename.split('.')[-1]
	myfilename = "%s.%s" % (uuid.uuid4(), ext)
	return f"podcast/audio/{myfilename}"

	


# def validate_file_extension(value):
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = ['.mp3', '.acc']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension.')
