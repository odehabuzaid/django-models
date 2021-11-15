from django.contrib.auth import get_user_model
from django.db import models


class Snack(models.Model):
    # Fields
    name = models.CharField(max_length=64, help_text="Enter Snack Name")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.name
