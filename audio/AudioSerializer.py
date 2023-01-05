from rest_framework import serializers
from .models import Audios


class AudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = ('id','name','language','zartist','annotation','avatar','audio')
        #read_only_fields = ['']


# class AudioSeria(serializers.Serializer):
