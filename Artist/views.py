from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Artist,Links,Subscribers,Action,UserFollowing
from .ArtistSerializer import ArtistSerializers
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


class ArtistList(APIView):
    def get(self,request,format=None):
        artist = Artist.objects.all()
        serializer = ArtistSerializers(artist,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self,request,*args,**kwargs):
        serializer = ArtistSerializers(data=request.data)
        if serializer.is_valid():
            artists = serializer.save()
            serializer = ArtistSerializers(serializer)
            print("This is where the error occurred")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArtistDetail(APIView):
    """
    Retrieve, update or delete a artist instance.
    """
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializers(artist)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializers(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        artist = self.get_object(pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


