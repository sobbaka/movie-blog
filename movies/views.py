from django.shortcuts import render
from django.views.generic.base import View

from .models import *

# Create your views here.

class MovieView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/base_movie_list.html', {'movie_list': movies})


class MovieDetail(View):

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, 'movies/base_movie_detail.html', {'movie': movie})