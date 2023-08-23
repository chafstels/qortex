from rest_framework import viewsets
from .models import Performer, Album, Song
from .serializers import PerformerSerializer, AlbumSerializer, SongSerializer


class PerformerViewSet(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer