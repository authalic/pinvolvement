from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Subject #, Contact, Comment, Organization


class SubjectForm(forms.ModelForm):
    # Form fields can go here, with added validators

    class Meta:
        model = Subject
        fields = ('__all__')
        widgets = {'coordinates': LeafletWidget()}