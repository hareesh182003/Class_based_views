from django import forms
from app.models import *
class VoterMF(forms.ModelForm):
    class Meta:
        model = Voter
        fields = '__all__'