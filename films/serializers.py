from rest_framework import serializers

class FilmSerializer(serializers.Serializer):
    title = serializers.CharField()
    type = serializers.CharField()
    titlereleased = serializers.CharField()
    image_landscape = serializers.CharField()
    image_portrait = serializers.CharField()
    rating = serializers.CharField()
    quality = serializers.CharField()
    actors = serializers.CharField()
    director = serializers.CharField()
    category = serializers.CharField()
    imdb = serializers.CharField()
    runtime = serializers.CharField()
    netflixid = serializers.CharField()
    date_released = serializers.CharField()
    description = serializers.CharField()
    language = serializers.CharField()
