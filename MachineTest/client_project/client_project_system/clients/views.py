from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

def api_tester(request):
    return render(request, 'index.html')


def home_view(request):
    return HttpResponse("Welcome to the Client Project System API")

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


# 1. Register a Client

class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        client_id = self.request.query_params.get('id')
        if client_id:
            return Client.objects.filter(id=client_id)
        return Client.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# 2. Fetch Client's Info
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.prefetch_related('projects')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
# 4. Add New Projects for a Client
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client_id = self.request.data.get('client')
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise ValidationError("Client with the given ID does not exist.")

        users = self.request.data.get('users')
        if not users:
            raise ValidationError("Users field is required.")

        user_instances = User.objects.filter(id__in=users)
        if not user_instances.exists():
            raise ValidationError("No valid users were found for the given IDs.")

        serializer.save(client=client, created_by=self.request.user)
        project_instance = serializer.instance
        project_instance.users.set(user_instances)

# 5. Retrieve Assigned Projects to Logged-in Users
class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
