from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Actor
from .models import ActorLookup	
from .models import Director
from .models import DirectorLookup
from .models import Writer
from .models import WriterLookup
from .models import Title

def index(request):
	return HttpResponse("Welcome. To the Movie DB")

class HomePageView(generic.TemplateView):
	template_name = 'movie_db/home.html'