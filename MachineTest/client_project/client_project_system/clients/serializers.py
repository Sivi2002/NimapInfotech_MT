from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True) 
    users = UserSerializer(many=True, read_only=True)
    user_ids = serializers.ListField(write_only=True, child=serializers.IntegerField(), required=False)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'users', 'user_ids', 'created_at', 'created_by_name','updated_at']
        read_only_fields = ['created_by', 'created_at','updated_at']

    def create(self, validated_data):
        user_ids = validated_data.pop('user_ids', None)
        project = Project.objects.create(**validated_data)

        if user_ids:
            users = User.objects.filter(id__in=user_ids)
            project.users.set(users)

        return project

class ClientSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()
    projects = ProjectSerializer(many=True, read_only=True)  # Include related projects

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by_name', 'created_at', 'projects']  # Include projects in the fields
        read_only_fields = ['created_by_name', 'created_at']

    def get_created_by_name(self, obj):
        return obj.created_by.username