import django_filters
from movie_db.models import Title, Actor, Writer, \
	Director, ActorLookup, WriterLookup, DirectorLookup


class TitleFilter(django_filters.FilterSet):
	primarytitle = django_filters.CharFilter(
		field_name='primarytitle',
		label='Film Title',
		lookup_expr='icontains'
	)

	genres = django_filters.CharFilter(
		field_name='genres',
		label='Genre(s)',
		lookup_expr='icontains'
	)

	rating = django_filters.NumericRangeFilter (
		field_name = 'averageRating',
		label = "IMDB Rating (Avg)",
		lookup_expr = 'icontains'

	)

	# Add description, heritage_site_category, region, sub_region and intermediate_region filters here

	# country_area = django_filters.ModelChoiceFilter(
	# 	field_name='country_area',
	# 	label='Country/Area',
	# 	queryset=CountryArea.objects.all().order_by('country_area_name'),
	# 	lookup_expr='exact'
	# )

	# Add date_inscribed filter here


	class Meta:
		model = Title
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []