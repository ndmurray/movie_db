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
	paginate_by = 50


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

	def get_queryset(self):
		return Title.objects.all() 

#Create, update, delete

#Create title
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
			for actor in form.cleaned_data['actor']:
				ActorLookup.objects.create(a_title=title, actor=actor)
			for director in form.cleaned_data['director']:
				DirectorLookup.objects.create(d_title=title, director=director)
			for writer in form.cleaned_data['writer']:
				WriterLookup.objects.create(w_title=title, writer=writer)
			print("valid entry")
			return redirect(title) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		print('not valid')
		print(form.errors)
		return render(request, 'movie_db/title_new.html', {'form': form})

	def get(self, request):
		form = TitleForm()
		return render(request, 'movie_db/title_new.html', {'form': form})

#Update Title
@method_decorator(login_required, name='dispatch')
class TitleUpdateView(generic.UpdateView):
	model = Title
	form_class = TitleForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'title_update' 
	# pk_url_kwarg = 'site_pk'
	success_message = "Film updated successfully"
	template_name = 'movie_db/title_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		title = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		title.save()

		# Current many to many values linked to title
		old_ids_a = ActorLookup.objects\
			.values_list('a_title', flat=True)\
			.filter(a_title=title.title_id)

		old_ids_d = DirectorLookup.objects\
			.values_list('d_title', flat=True)\
			.filter(d_title=title.title_id)

		old_ids_w = WriterLookup.objects\
			.values_list('w_title', flat=True)\
			.filter(w_title=title.title_id)

		# New lists
		new_actors = form.cleaned_data['actor']
		new_directors = form.cleaned_data['director']
		new_writers = form.cleaned_data['writer']

		# TODO can these loops be refactored?

		# New ids
		new_ids_a = []
		new_ids_d = []
		new_ids_w = []

		# Insert new unmatched new entries
		for actor in new_actors:
			new_id_a = actor.actor_id
			new_ids_a.append(new_id_a)
			if new_id_a in old_ids_a:
				continue
			else:
				ActorLookup.objects \
					.create(a_title=title, actor=actor)

		for director in new_directors:
			new_id_d = director.director_id
			new_ids_d.append(new_id_d)
			if new_id_d in old_ids_d:
				continue
			else:
				DirectorLookup.objects \
					.create(d_title=title, director=director)

		for writer in new_writers:
			new_id_w = writer.writer_id
			new_ids_w.append(new_id_w)
			if new_id_w in old_ids_w:
				continue
			else:
				WriterLookup.objects \
					.create(w_title=title, writer=writer)

		# Delete old unmatched entries
		for old_id_a in old_ids_a:
			if old_id_a in new_ids_a:
				continue
			else:
				ActorLookup.objects \
					.filter(a_title=title.title_id, actor=old_id_a) \
					.delete()

		for old_id_d in old_ids_d:
			if old_id_d in new_ids_d:
				continue
			else:
				DirectorLookup.objects \
					.filter(d_title=title.title_id, director=old_id_d) \
					.delete()

		for old_id_w in old_ids_w:
			if old_id_w in new_ids_w:
				continue
			else:
				WriterLookup.objects \
					.filter(w_title=title.title_id, writer=old_id_w) \
					.delete()


		return HttpResponseRedirect(title.get_absolute_url())
		# return redirect('heritagesites/site_detail', pk=site.pk)

#Delete Title
@method_decorator(login_required, name='dispatch')
class TitleDeleteView(generic.DeleteView):
	model = Title
	success_message = "Title deleted successfully"
	success_url = '/movie_db'
	context_object_name = 'title'
	template_name = 'movie_db/title_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete many to many entries
		ActorLookup.objects \
			.filter(a_title_id=self.object.title_id) \
			.delete()

		DirectorLookup.objects \
			.filter(d_title_id=self.object.title_id) \
			.delete()

		WriterLookup.objects \
			.filter(w_title_id=self.object.title_id) \
			.delete()


		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())
