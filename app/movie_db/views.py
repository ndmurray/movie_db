from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django_filters.views import FilterView

from .models import Actor
from .models import ActorLookup	
from .models import Director
from .models import DirectorLookup
from .models import Writer
from .models import WriterLookup
from .models import Title

from .forms import TitleForm
from .filters import TitleFilter

def index(request):
	return HttpResponse("Welcome. To the Movie DB")

class HomePageView(FilterView):
	context_object_name = 'home'
	template_name = 'movie_db/home.html'
	filterset_class = TitleFilter

# class TitleFilterView(FilterView):
# 	template_name = 'movie_db/home.html'