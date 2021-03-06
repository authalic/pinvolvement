from django import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Subject, Comment, Contact, Organization


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'


class SubjectForm(forms.ModelForm):

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
            'commentxt': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 8}),
            'attachment': forms.FileInput(attrs={'class': 'form-control'}),
        }
