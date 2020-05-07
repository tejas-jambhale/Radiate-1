from .models import Team
from django import forms


class TeamForm(forms.Form):
    team_name = forms.CharField()
