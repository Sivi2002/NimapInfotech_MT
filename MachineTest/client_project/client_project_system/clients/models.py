from django.db import models
from django.contrib.auth.models import User

#define your models here

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.client_name
    class Meta:
        db_table = "Nimap_Client"

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
    class Meta:
        db_table = "Nimap_Project"