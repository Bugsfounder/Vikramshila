from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=120, unique=True, primary_key=True)
    description = models.TextField()
    slug = models.SlugField(max_length = 250, null = False, blank = False)
    image = models.ImageField(upload_to="jobs/category", null=True, blank=True)
    datetime = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title

class Job(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    price= models.IntegerField()
    datetime = datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
  