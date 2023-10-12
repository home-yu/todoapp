from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField("title",max_length=20)
    description = models.TextField("description",blank=True)
    deadline = models.DateField("deadline")

    def __str__(self) -> str:
        return self.title