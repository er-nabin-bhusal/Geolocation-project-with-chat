from photos.models import Picture

from django import forms

class PictureForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ['caption','photo']