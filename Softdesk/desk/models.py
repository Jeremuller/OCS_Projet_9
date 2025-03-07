from django.db import models

from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_projects")


class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")
    role = models.CharField(max_length=100, choices=["AUTHOR", 'CONTRIBUTOR'], default="CONTRIBUTOR")

    class Meta:
        unique_together = ('user', 'project')
