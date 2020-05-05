from .models import Team
from django import forms


class TeamForm(forms.Form):
    team_name = forms.CharField()
    set_number = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
