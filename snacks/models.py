from django.db import models


class Snack(models.Model):
    """Snacks app model ,derived from the Model class."""

    # Fields
    name = models.CharField(max_length=64, help_text="Enter Snack Name")
    purchaser = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    description = models.TextField()
    ...

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
