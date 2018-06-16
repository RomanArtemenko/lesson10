from django.db import models

# Create your models here.
class Shortly(models.Model):
    link = models.URLField(unique=True)
    visit_counter = models.PositiveIntegerField(default=0)