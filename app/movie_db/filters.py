import django_filters
from movie_db.models import Title, Actor, Writer, \
	Director, ActorLookup, WriterLookup, DirectorLookup


class TitleFilter(django_filters.FilterSet):
	primarytitle = django_filters.CharFilter(
		field_name='primarytitle',
		label='Title(s)',
		lookup_expr='icontains'
	)

	genres = django_filters.CharFilter(
		field_name='genres',
		label='Genre(s)',
		lookup_expr='icontains'
	)

	genres = django_filters.CharFilter(
		field_name='genres',
		label='Genre(s)',
		lookup_expr='icontains'
	)

	actors = django_filters.CharFilter(
		field_name='actorlookup__actor__primaryname',
		label='Actor(s)',
		lookup_expr='icontains'
	)

	directors = django_filters.CharFilter(
		field_name='directorlookup__director__primaryname',
		label='Director(s)',
		lookup_expr='icontains'
	)

	writers = django_filters.CharFilter(
		field_name='writerlookup__writer__primaryname',
		label='Writer(s)',
		lookup_expr='icontains'
	)

	class Meta:
		model = Title
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []

# class ActorFilter(django_filters.FilterSet):		
# 	actor = django_filters.CharFilter(
# 		field_name='primaryname',
# 		label='Actor(s)',
# 		lookup_expr='icontains'
# 	)

# 	class Meta:
# 		model = Actor
# 		# form = SearchForm
# 		# fields [] is required, even if empty.
# 		fields = []

	
	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here

	# country_area = django_filters.ModelChoiceFilter(
	# 	field_name='country_area',
	# 	label='Country/Area',
	# 	queryset=CountryArea.objects.all().order_by('country_area_name'),
	# 	lookup_expr='exact'
	# )

	# Add date_inscribed filter here


