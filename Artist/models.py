from django.db import models
from django.conf import settings
from django.core.validators import URLValidator
from account.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from meta.models import Country


class Artist(models.Model):
    user_acc = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    artist_name = models.CharField(max_length=25,)
    country = models.ForeignKey(Country,related_name='country',on_delete=models.CASCADE)

    def __str__(self):
        return self.user_acc.username


class Links(models.Model):
    zArtist = models.ForeignKey(Artist,related_name='socialmedialinks',on_delete=models.CASCADE)
    link = models.URLField(max_length=200,validators=[URLValidator])
    link_description = models.CharField(max_length=15)

    def __str__(self):
        return self.link_description


class Subscribers(models.Model):
    musician_id = models.ForeignKey(Artist,related_name='subscribers',on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User,related_name='subscription', on_delete=models.CASCADE)


# generic activity stream
class Action(models.Model):
    nushauser = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='actions',
                                  db_index=True,on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,blank=True,null=True,
                      related_name='target_obj',on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.nushauser.username + " " + self.verb

    class Meta:
        ordering = ('-created',)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following",on_delete=models.CASCADE,db_index=True)
    following_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="followers",on_delete=models.CASCADE,db_index=True)

    def __str__(self):
        return self.user_id.username + " following " + self.following_user_id.username
