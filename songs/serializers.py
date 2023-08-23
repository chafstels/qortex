from rest_framework import serializers
from .models import Performer, Album, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'sequence_number']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['title', 'production_year', 'songs']

class PerformerSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Performer
        fields = ['name', 'albums']