from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django_filters.views import FilterView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

@method_decorator(login_required, name='dispatch')
class HomePageView(FilterView):
	model = Title
	context_object_name = 'home'
	template_name = 'movie_db/home.html'
	filterset_class = TitleFilter

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return Title.objects.all() 

# class TitleFilterView(FilterView):
# 	template_name = 'movie_db/home.html'


@method_decorator(login_required, name='dispatch')
class FilmDetailView(generic.DetailView):
	model = Title
	context_object_name = 'film_detail'
	template_name = 'movie_db/film_detail.html'
	filterset_class = TitleFilter

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

#Create, update, delete
@method_decorator(login_required, name='dispatch')
class TitleCreateView(generic.View):
	model = Title
	form_class = TitleForm
	success_message = "Title created successfully"
	template_name = 'movie_db/title_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = TitleForm(request.POST)
		if form.is_valid():
			title = form.save(commit=False)
			title.save()
			for actor in form.cleaned_data['actors']:
				ActorLookup.objects.create(a_title=title, actor=actor)
			for director in form.cleaned_data['directors']:
				DirectorLookup.objects.create(d_title=title, director=actor)
			for writer in form.cleaned_data['writers']:
				WriterLookup.objects.create(w_title=title, writer=actor)
			return redirect(title) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'movie_db/title_new.html', {'form': form})

	def get(self, request):
		form = TitleForm()
		return render(request, 'movie_db/title_new.html', {'form': form})