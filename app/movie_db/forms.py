from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from movie_db.models import Title, Actor, Writer, Director, ActorLookup, WriterLookup, DirectorLookup


class TitleForm(forms.ModelForm):
	class Meta:
		model = Title
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'submit'))

# class ActorForm(forms.ModelForm):
# 	class Meta:
# 		model = Actor
# 		fields = '__all__'

# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.helper = FormHelper()
# 		self.helper.form_method = 'post'
# 		self.helper.add_input(Submit('submit', 'submit'))