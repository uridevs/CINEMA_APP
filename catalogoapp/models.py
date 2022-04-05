from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Films(models.Model):
    author = models.ForeignKey(Director, default=None, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    sinopsis = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

