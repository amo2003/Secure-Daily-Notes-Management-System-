from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print("Creating user with data:", validated_data)
        try:
            user = User.objects.create_user(**validated_data)
            print("User created successfully:", user.username)
            return user
        except Exception as e:
            print("Error in create method:", str(e))
            raise serializers.ValidationError({"error": f"Failed to create user: {str(e)}"})


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}