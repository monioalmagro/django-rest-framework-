from rest_framework import serializers
from djanfo.contrib.auth.models import user

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    firts_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers,EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filters(username = data)
        if len(user) != 0:
            raise serializers.ValidationError("Este nombre ya existe , ingrese uno nuevo")
        else:
            return data
