from rest_framework import serializers
from .models import Movie, Director, Actor, Genre, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'bio']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)  # Acepta múltiples actores
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)  # Acepta múltiples géneros

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'director', 'actors', 'genres']

    def create(self, validated_data):
        director_data = validated_data.pop('director')  # Extraer el director
        director = Director.objects.create(**director_data)  # Crear el director

        actors_data = validated_data.pop('actors')  # Extraer actores
        genres_data = validated_data.pop('genres')  # Extraer géneros

        movie = Movie.objects.create(director=director, **validated_data)  # Crear la película

        # Asociar actores y géneros a la película
        movie.actors.set(actors_data)
        movie.genres.set(genres_data)

        return movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'content', 'created_at']
