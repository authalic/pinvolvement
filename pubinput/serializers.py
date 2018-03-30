from rest_framework import serializers
from pubinput.models import PublicComment

# This needs to extend Serializer. Don't use ModelSerializer
# Some of the fields need to be set to allow blank or null as a valid post

class CommentSerializer(serializers.Serializer):
    comment= serializers.CharField(style={'input_type': 'textarea'})
    first_name = serializers.CharField(allow_blank=True, allow_null=True)
    last_name = serializers.CharField(allow_blank=True, allow_null=True) 
    email = serializers.EmailField(max_length=None, min_length=None, required=False, allow_blank=True)
    phone = serializers.CharField(allow_blank=True, allow_null=True)
    address1 = serializers.CharField(allow_blank=True, allow_null=True)
    address2 = serializers.CharField(allow_blank=True, allow_null=True)
    city = serializers.CharField(allow_blank=True, allow_null=True)
    state = serializers.CharField(allow_blank=True, allow_null=True)
    zipcode = serializers.CharField(allow_blank=True, allow_null=True)
    location = serializers.CharField(allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return PublicComment.objects.create(**validated_data)

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicComment
        fields = (
            'comment', 
            'submitted', 
            'location', 
        )
