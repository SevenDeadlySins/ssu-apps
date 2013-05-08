from django.db import models

# Create your models here.


class Tour(models.Model):
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

    tour_name = models.CharField(max_length=50)
    tour_count = models.IntegerField()

    def __unicode__(self):
        pass
