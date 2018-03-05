from rest_framework import serializers
from pubinput.models import PublicComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicComment
        fields = (
            'comment', 
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'address1', 
            'address2', 
            'city', 
            'state', 
            'zipcode', 
            'submitted', 
            'location', 
            'bcookie'
            )


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicComment
        fields = (
            'comment', 
            'submitted', 
            'location', 
        )