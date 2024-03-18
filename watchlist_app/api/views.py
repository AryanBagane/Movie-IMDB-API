from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response


def Movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def movies_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)