from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from .spotify_recommender import getRecById


def index(request):
    return HttpResponse("Hello, world. You're at the ocarina index.")
# Create your views here.

class SongRecommendationView(View):
    def get(self, request):
        songs = request.GET.getlist('songs')
        artists = request.GET.getlist('artists', [])
        genres = request.GET.getlist('genres', [])
        limit = int(request.GET.get('limit', 5))

        recommendations = getRecById(songs, artists, genres, limit)

        if recommendations:
            response_data = [
                {'name' : track['name'], 'artist': track['artists'][0]['name']}
                for track in recommendations
            ]
            return JsonResponse(response_data, safe = False)
        else:
            return JsonResponse({'error' : 'No Recommendations found'}, status = 404)
        