from movie_db.models import Title, Actor, ActorLookup, Director, \
	DirectorLookup, Writer, WriterLookup
from rest_framework import response, serializers, status


class ActorLookupSerializer(serializers.ModelSerializer):
	actor_id = serializers.ReadOnlyField(source='actor.actor_id')
	a_title_id = serializers.ReadOnlyField(source='title.title_id')

	class Meta:
		model = ActorLookup
		fields = ('actor_id', 'a_title_id')

class DirectorLookupSerializer(serializers.ModelSerializer):
	director_id = serializers.ReadOnlyField(source='director.director_id')
	d_title_id = serializers.ReadOnlyField(source='title.title_id')

	class Meta:
		model = DirectorLookup
		fields = ('director_id', 'd_title_id')

class WriterLookupSerializer(serializers.ModelSerializer):
	writer_id = serializers.ReadOnlyField(source='writer.writer_id')
	w_title_id = serializers.ReadOnlyField(source='title.title_id')

	class Meta:
		model = WriterLookup
		fields = ('writer_id', 'w_title_id')



class ActorSerializer(serializers.ModelSerializer):
	actor_id = ActorLookupSerializer(many=False, read_only=True)

	class Meta:
		model = Actor
		fields = (
			'actor_id',
			'primaryname',
			'birthyear',
			'deathyear',
			'knownfortitles')

class DirectorSerializer(serializers.ModelSerializer):
	director_id = DirectorLookupSerializer(many=False, read_only=True)

	class Meta:
		model = Director
		fields = (
			'director_id',
			'primaryname',
			'birthyear',
			'deathyear',
			'knownfortitles')

class WriterSerializer(serializers.ModelSerializer):
	writer_id = WriterLookupSerializer(many=False, read_only=True)

	class Meta:
		model = Writer
		fields = (
			'writer_id',
			'primaryname',
			'birthyear',
			'deathyear',
			'knownfortitles')


class TitleSerializer(serializers.ModelSerializer):
	title_id = serializers.CharField(
		allow_blank=False,
		max_length=255
	)
	titletype = serializers.CharField(
		allow_blank=True,
		max_length=255
	)
	primarytitle = serializers.CharField(
		allow_blank=False,
		max_length=255
	)
	originaltitle = serializers.CharField(
		allow_blank=True,
		max_length=255
	)
	isadult = serializers.IntegerField(
		allow_null=True,
	)
	startyear = serializers.CharField(
		allow_blank=True,
		max_length=4
	)
	endyear = serializers.CharField(
		allow_blank=True,
		max_length=4
	)
	runtimeminutes = serializers.CharField(
		allow_blank=True,
		max_length=255
	)
	genres = serializers.CharField(
		allow_blank=True,
		max_length=255
	)
	averagerating = serializers.FloatField(
		allow_null=True,
	)
	numvotes = serializers.IntegerField(
		allow_null=True,
	)
	actors = ActorLookupSerializer(
		source='actor_lookup_set', # Note use of _set
		many=True,
		read_only=True
	)
	directors = DirectorLookupSerializer(
		source='director_lookup_set', # Note use of _set
		many=True,
		read_only=True
	)
	writers = WriterLookupSerializer(
		source='writer_lookup_set', # Note use of _set
		many=True,
		read_only=True
	)

	actor_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Actor.objects.all(),
		source='actor_lookup'
	)

	director_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Director.objects.all(),
		source='director_lookup'
	)

	writer_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Writer.objects.all(),
		source='director_lookup'
	)

	class Meta:
		model = Title
		fields = (
			'title_id',
			'titletype',
			'primarytitle',
			'originaltitle',
			'isadult',
			'startyear',
			'endyear',
			'runtimeminutes',
			'genres',
			'averagerating',
			'numvotes',
			'actors',
			'directors',
			'writers',
			'actor_ids',
			'director_ids',
			'writer_ids'

		)
	def create(self, validated_data):
	

		# print(validated_data)

		actors = validated_data.pop('actor_lookup')
		directors = validated_data.pop('director_lookup')
		writers = validated_data.pop('writer_lookup')

		title = Title.objects.create(**validated_data)

		if actors is not None:
			for actor in actors:
				ActorLookup.objects.create(
					actor_id=actor.actor_id,
					a_title_id=title.title_id
				)

		return title

		if director is not None:
			for director in directors:
				DirectorLookup.objects.create(
					director_id=director.director_id,
					d_title_id=title.title_id
				)

		return title

		if writer is not None:
			for writer in writers:
				WriterLookup.objects.create(
					writer_id=writer.writer_id,
					w_title_id=title.title_id
				)

		return title

	def update(self, instance, validated_data):
		# site_id = validated_data.pop('heritage_site_id')
		title_id = instance.title_id
		new_actors = validated_data.pop('actor_lookup')
		new_directors = validated_data.pop('director_lookup')
		new_writers = validated_data.pop('writer_lookup')

		instance.title_id = validated_data.get(
			'title_id',
			instance.title_id
		)
		instance.titletype = validated_data.get(
			'titletype',
			instance.titletype
		)
		instance.primarytitle = validated_data.get(
			'primarytitle',
			instance.primarytitle
		)
		instance.originaltitle = validated_data.get(
			'originaltitle',
			instance.originaltitle
		)
		instance.isadult = validated_data.get(
			'isadult',
			instance.isadult
		)
		instance.startyear = validated_data.get(
			'startyear',
			instance.startyear
		)
		instance.endyear = validated_data.get(
			'endyear',
			instance.endyear
		)
		instance.runtimeminutes = validated_data.get(
			'runtimeminutes',
			instance.runtimeminutes
		)
		instance.genres = validated_data.get(
			'genres',
			instance.genres
		)
		instance.averagerating = validated_data.get(
			'averagerating',
			instance.averagerating
		)
		instance.numvotes = validated_data.get(
			'numvotes',
			instance.numvotes
		)

		instance.save()

		# If any existing actors, directors, writres are not in updated list, delete them
		new_ids_a = []#
		old_ids_a = ActorLookup.objects \
			.values_list('actor_id', flat=True) \
			.filter(title_id__exact=title_id)

		# TODO Insert may not be required (Just return instance)

		# Insert new unmatched country entries
		for actor in new_actors:#
			new_id_a = actor.actor_id#
			new_ids_a.append(new_id_a)
			if new_id_a in old_ids_a:
				continue
			else:#
				ActorLookup.objects \
					.create(title_id=title_id, actor_id=new_id_a)#

		# Delete old unmatched country entries
		for old_id_a in old_ids_a:
			if old_id_a in new_ids_a:
				continue
			else:#
				ActorLookup.objects \
					.filter(title_id=title_id, actor_id=new_id_a) \
					.delete()

		new_ids_d = []#
		old_ids_d = DirectorLookup.objects \
			.values_list('director_id', flat=True) \
			.filter(title_id__exact=title_id)

		# TODO Insert may not be required (Just return instance)

		# Insert new unmatched country entries
		for director in new_directors:#
			new_id_d = director.director_id#
			new_ids_d.append(new_id_d)
			if new_id_d in old_ids_d:
				continue
			else:#
				DirectorLookup.objects \
					.create(title_id=title_id, director_id=new_id_d)#

		# Delete old unmatched country entries
		for old_id_d in old_ids_d:
			if old_id_d in new_ids_d:
				continue
			else:#
				DirectorLookup.objects \
					.filter(title_id=title_id, director_id=new_id_d) \
					.delete()

		new_ids_w = []#
		old_ids_w = WriterLookup.objects \
			.values_list('writer_id', flat=True) \
			.filter(title_id__exact=title_id)

		# TODO Insert may not be required (Just return instance)

		# Insert new unmatched country entries
		for writer in new_writers:#
			new_id_w = writer.writer_id#
			new_ids_w.append(new_id_w)
			if new_id_w in old_ids_w:
				continue
			else:#
				WriterLookup.objects \
					.create(title_id=title_id, writer_id=new_id_w)#

		# Delete old unmatched country entries
		for old_id_w in old_ids_w:
			if old_id_w in new_ids_w:
				continue
			else:#
				WriterLookup.objects \
					.filter(title_id=title_id, writer_id=new_id_w) \
					.delete()

		return instance



