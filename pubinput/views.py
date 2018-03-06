from pubinput.models import PublicComment
from pubinput.serializers import CommentSerializer, ViewSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

# Create your views here.


class CommentList(LoginRequiredMixin, generics.ListCreateAPIView):
    '''
    List all Comments or create a new Comment (login required)
    '''
    queryset = PublicComment.objects.all()
    serializer_class = CommentSerializer


class CommentView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a comment (login required)
    '''
    queryset = PublicComment.objects.all()
    serializer_class = CommentSerializer


class CommentListOnly(generics.ListAPIView):
    '''
    Endpoint to GET all Comments (redacted). 
    No other request types permitted.
    Fields are limited to comment, location, and date/time submitted.
    '''
    queryset = PublicComment.objects.all()  
    serializer_class =  ViewSerializer  # change this serializer


class CommentCreateOnly(generics.CreateAPIView):
    '''
    Endpoint for public to POST Comments. No other request types permitted.
    '''
    queryset = PublicComment.objects.all()  
    serializer_class = CommentSerializer  # change this serializer
