from pubinput.models import PublicComment
from pubinput.serializers import CommentSerializer
from rest_framework import generics

# Create your views here.


class CommentList(generics.ListCreateAPIView):
    '''
    List all Comments or create a new Comment
    '''
    queryset = PublicComment.objects.all()
    serializer_class = CommentSerializer


class CommentView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update, or delete a comment
    '''
    queryset = PublicComment.objects.all()
    serializer_class = CommentSerializer
