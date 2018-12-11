# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Actor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actor'
        ordering = ['primaryname']
        verbose_name = 'Actor name'
        verbose_name_plural = 'Actors names'

    def __str__(self):
        return self.primaryname


class ActorLookup(models.Model):
    actor_lookup_id = models.AutoField(primary_key=True)
    #CHANGED FROM INTEGERFIELD, did the same to directorlookup and writerlookup models
    #actor_lookup_id = models.IntegerField(primary_key=True)
    actor = models.ForeignKey(Actor, models.DO_NOTHING)
    a_title = models.ForeignKey('Title', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actor_lookup'
        ordering = ['a_title','actor']
        verbose_name = 'Actor lookup value'
        verbose_name_plural = 'Actor lookup values'


class Director(models.Model):
    director_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'director'
        ordering = ['primaryname']
        verbose_name = 'Director name'
        verbose_name_plural = 'Directors names'

    def __str__(self):
        return self.primaryname


class DirectorLookup(models.Model):
    director_lookup_id = models.AutoField(primary_key=True)
    d_title = models.ForeignKey('Title', models.DO_NOTHING)
    director = models.ForeignKey(Director, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'director_lookup'
        ordering = ['d_title','director']
        verbose_name = 'Director lookup value'
        verbose_name_plural = 'Director lookup values'

class Writer(models.Model):
    writer_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'writer'
        ordering = ['primaryname']
        verbose_name = 'Writer name'
        verbose_name_plural = 'Writers names'

    def __str__(self):
        return self.primaryname


class WriterLookup(models.Model):
    writer_lookup_id = models.AutoField(primary_key=True)
    w_title = models.ForeignKey('Title', models.DO_NOTHING)
    writer = models.ForeignKey(Writer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'writer_lookup'
        ordering = ['w_title','writer']
        verbose_name = 'Writer lookup value'
        verbose_name_plural = 'Writer lookup values'

class Title(models.Model):
    title_id = models.CharField(primary_key=True, max_length=10)
    titletype = models.CharField(db_column='titleType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    primarytitle = models.CharField(db_column='primaryTitle', max_length=500)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isadult = models.IntegerField(db_column='isAdult', blank=True, null=True)  # Field name made lowercase.
    startyear = models.CharField(db_column='startYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='endYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.CharField(db_column='runtimeMinutes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(max_length=255, blank=True, null=True)
    averagerating = models.FloatField(db_column='averageRating', blank=True, null=True)  # Field name made lowercase.
    numvotes = models.IntegerField(db_column='numVotes', blank=True, null=True)  # Field name made lowercase.

    #Intermediate model fields
    actor = models.ManyToManyField(Actor, through='ActorLookup')
    director = models.ManyToManyField(Director, through='DirectorLookup')
    writer = models.ManyToManyField(Writer, through='WriterLookup')

    class Meta:
        managed = False
        db_table = 'title'
        ordering = ['-averagerating']
        verbose_name = 'Film title'
        verbose_name_plural = 'Film names'

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})

    def __str__(self):
        return self.primarytitle + ", " + self.startyear + " " + self.averagerating

    @property
    def director_names(self):

        directors = self.director.order_by('primaryname')

        names = []
        for director in directors:
            if director is None:
                continue
            name = director.primaryname
            if name is None:
                continue
            if name not in names:
                names.append(name)

        return ', '.join(names)

    @property
    def actor_names(self):

        actors = self.actor.order_by('primaryname')

        names = []
        for actor in actors:
            if actor is None:
                continue
            name = actor.primaryname
            if name is None:
                continue
            if name not in names:
                names.append(name)

        return ', '.join(names)

    @property
    def writer_names(self):

        writers = self.writer.order_by('primaryname')

        names = []
        for writer in writers:
            if writer is None:
                continue
            name = writer.primaryname
            if name is None:
                continue
            if name not in names:
                names.append(name)

        return ', '.join(names)