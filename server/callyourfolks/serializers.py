from callyourfolks.models import User, Contact, Call, Avatar
from rest_framework import serializers

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('id', 'contact', 'date', 'happened', 'recommended')
        depth = 1

class ContactSerializer(serializers.ModelSerializer):
    calls = CallSerializer(many=True)
    class Meta:
        model = Contact
        fields = ('id', 'user', 'calls', 'avatar', 'name', 'period')

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'contacts')

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id', 'url')
