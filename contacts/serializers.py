from rest_framework import serializers
from contacs.models import Contact

class ContactSerializer(serializers.Serializer):
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