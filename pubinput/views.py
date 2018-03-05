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
    List all comments only. No other request types allowed
    Fields are limited to comment, location, and date submitted
    This is the "redacted" view of the data that will appear on the comment map
    '''
    queryset = PublicComment.objects.all()  
    serializer_class =  ViewSerializer  # change this serializer


class CommentCreateOnly(generics.CreateAPIView):
    '''
    Endpoint for creating Comments. No other request types allowed
    '''
    queryset = PublicComment.objects.all()  
    serializer_class = CommentSerializer  # change this serializer
