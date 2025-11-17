from django.db import models

class Movies(models.Model):
    identification = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    director_name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    synopsis = models.TextField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.title
    