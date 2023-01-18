from concert.models import Concert, Artist
from rest_framework import serializers


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Concert
        # Поля, которые мы сериализуем
        fields = ["pk", "artist_id", "price", "address", "date", "descr", "age_rating", "pic"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Artist
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "descr", "avatar"]
