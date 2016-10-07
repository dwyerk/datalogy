from django import forms
from . import models

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = models.Challenge
        fields = ['name', 'description']