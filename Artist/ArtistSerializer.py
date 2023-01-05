from rest_framework import serializers
from .models import Artist,Links,Subscribers,Action,UserFollowing


class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','biography','artist_name','likes','user_acc','country')
