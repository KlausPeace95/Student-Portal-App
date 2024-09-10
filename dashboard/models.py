from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notes(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    # Returns title of Notes
    def __str__(self):
        return self.title

    # To remove Extra "s" on the Notes in Admin Panel
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

class Homework(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    # Returns the subject and title of Homework
    def __str__(self):
        return self.title

    # # To remove Extra "s" on the Homework in Admin Panel
    # class Meta:
    #     verbose_name = "homework"
    #     verbose_name_plural = "homework"

class Todo(models.Model):
    objects = None
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title


