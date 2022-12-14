from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    # due_date = models.DateTimeField(aut
    def __str__(self) -> str:
        return self.title