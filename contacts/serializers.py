from rest_framework import serializers
from contacts.models import Contact, Comment

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__' )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields= ('__all__')
