from django.db import models
from utils import saveMoodImage
from django.core.validators import FileExtensionValidator


class Country(models.Model):
    name = models.CharField(max_length = 29)

    def __str__(self):
    	return self.name 


class Moods(models.Model):
    name = models.CharField(max_length = 29)
    avatar = models.ImageField(upload_to=saveMoodImage, 
    	      validators=[FileExtensionValidator(allowed_extensions=["jpg","png","jpeg"])], null=True, blank=True)

    def __str__(self):
    	return self.name 


class Language(models.Model):
    name = models.CharField(max_length = 29)

    def __str__(self):
    	return self.name 


class Genre(models.Model):
    name = models.CharField(max_length = 29)

    def __str__(self):
    	return self.name 


class Tag(models.Model):
    name = models.CharField(max_length = 29)

    def __str__(self):
    	return self.name 




