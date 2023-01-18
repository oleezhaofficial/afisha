from rest_framework import viewsets
from concert.serializers import ConcertSerializer, ArtistSerializer
from django.shortcuts import render
from .models import Artist, Concert
from django.http import HttpResponse


def GetMenu(request):
    concert = Concert.objects.all()
    context = {
        'concert': concert
    }
    return render(request, 'menu.html', context)


def GetArtist(request, pk):
    artist = Artist.objects.get(id=pk)
    concert = Concert.objects.all()
    context = {
        'artist': artist,
        'concert': concert
    }
    return render(request, 'artist.html', context)


def GetAllArtistAllConcerts(request):
    artist = Artist.objects.all()
    concert = Concert.objects.all()
    context = {
        'artist': artist,
        'concert': concert
    }
    return render(request, 'artistsconcerts.html', context)


def GetAllArtists(request):
    artist = Artist.objects.all()
    context = {
        'artist': artist
    }
    return render(request, 'allartists.html', context)


def GetConcert(request):
    concert = Concert.objects.all()
    context = {
        'concert': concert
    }
    return render(request, 'concert.html', context)


def GetExactConcert(request, pk):
    concert = Concert.objects.get(id=pk)
    context = {
        'concert': concert
    }
    return render(request, 'exactconcert.html', context)
























class ConcertViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать мероприятия
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Concert.objects.all().order_by('date')
    serializer_class = ConcertSerializer  # Сериализатор для модели


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать артистов
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer  # Сериализатор для модели
