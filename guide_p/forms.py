from django import forms


class StationForm(forms.Form):
    station = forms.CharField(min_length=3, max_length=20)
    line = forms.CharField(min_length=3, max_length=200)
    admarea = forms.IntegerField(min_value=3, max_value=100000)
    district = forms.CharField(min_length=3, max_length=200)
    status = forms.CharField(min_length=3, max_length=200)


