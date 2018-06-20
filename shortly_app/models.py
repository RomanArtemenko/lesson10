from django.db import models

# Create your models here.
class Top5ShortlyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(visit_counter__gt=0).order_by('-visit_counter')[:5]
    
class Shortly(models.Model):
    link = models.URLField(unique=True)
    visit_counter = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    top5 = Top5ShortlyManager()

    def update_counter(self):
        self.visit_counter += 1 
        self.save()
