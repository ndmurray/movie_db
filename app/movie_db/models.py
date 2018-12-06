# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actor'


class ActorLookup(models.Model):
    actor_lookup_id = models.IntegerField(primary_key=True)
    actor = models.ForeignKey(Actor, models.DO_NOTHING)
    a_title = models.ForeignKey('Title', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actor_lookup'


class Director(models.Model):
    director_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'director'


class DirectorLookup(models.Model):
    director_lookup_id = models.IntegerField(primary_key=True)
    d_title = models.ForeignKey('Title', models.DO_NOTHING)
    director = models.ForeignKey(Director, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'director_lookup'


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

    class Meta:
        managed = False
        db_table = 'title'


class Writer(models.Model):
    writer_id = models.CharField(primary_key=True, max_length=10)
    primaryname = models.CharField(db_column='primaryName', max_length=255)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'writer'


class WriterLookup(models.Model):
    writer_lookup_id = models.IntegerField(primary_key=True)
    w_title = models.ForeignKey(Title, models.DO_NOTHING)
    writer = models.ForeignKey(Writer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'writer_lookup'
