from django.db import models

from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_projects")

    PROJECT_TYPES = [
        ("BACKEND", "Back-end"),
        ("FRONTEND", "Front-end"),
        ("IOS", "iOS"),
        ("ANDROID", "Android"),
    ]
    type = models.CharField(max_length=10, choices=PROJECT_TYPES, default="BACKEND")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributions")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="contributors")

    ROLE_CHOICES = [
        ("AUTHOR", "Author"),
        ("CONTRIBUTOR", "Contributor"),
    ]

    role = models.CharField(max_length=11, choices=ROLE_CHOICES, default="CONTRIBUTOR")

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} -> {self.project.name} ({self.role})"
