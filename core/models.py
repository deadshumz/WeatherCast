from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class FavoriteCity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Favorite city'
        verbose_name_plural = "Favorite cities"