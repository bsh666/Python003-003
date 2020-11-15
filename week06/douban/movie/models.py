from django.db import models

# Create your models here.


class MovieModel(models.Model):
    name = models.CharField("Movie", max_length=155, db_index=True)
    published_date = models.DateField("Publish date", null=True)
    description = models.TextField("Description of movie")
    stars = models.FloatField("Stars", default=0)

    class Meta:
        app_label = "movie"
        db_table = "movie"

    def __str__(self):
        return f"{self.description}"