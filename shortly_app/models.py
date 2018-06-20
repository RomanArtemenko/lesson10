from django.db import models

# Create your models here.
class TopShortlyManager(models.Manager):
    def top(self, count=5):
        return super().get_queryset().filter(visit_counter__gt=0).order_by('-visit_counter')[:count]
    
class Shortly(models.Model):
    link = models.URLField(unique=True)
    visit_counter = models.PositiveIntegerField(default=0)

    objects = TopShortlyManager()

    def update_counter(self):
        self.visit_counter += 1 
        self.save()