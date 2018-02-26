from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Subject, Comment #, Contact, Organization


class SubjectForm(forms.ModelForm):
    # Form fields can go here, with added validators

    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.Select(attrs={'class': 'form-control'}),
            'initial_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'coordinates': LeafletWidget(),
        }


class CommentForm(forms.ModelForm):
    # Form fields can go here, with added validators

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'contact': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-control'}),
            'method': forms.Select(attrs={'class': 'form-control'}),
            'comment_datetime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'commentxt': forms.TextInput(attrs={'class': 'form-control'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
        }