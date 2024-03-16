# Create your models here.
from django.db import models

# Create your models here.
class Issue(models.Model):
    """
    Issue Model.
    """
    
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Title to be  returned as object reference.
        """
        return self.title
