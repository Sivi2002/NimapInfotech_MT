from django.urls import path
from .views import (
    ClientListCreateView,
    ClientDetailView,
    ProjectCreateView,
    UserProjectsView,
    UserCreateView,
    api_tester,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    
    path('projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/my/', UserProjectsView.as_view(), name='user-projects'),
    path('api-tester/', api_tester, name='api-tester'),
]