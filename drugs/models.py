from django.db import models

# Create your models here.


class Drug(models.Model):
    name = models.CharField(max_length=100)
    #category =
    quantity = models.IntegerField()
    price = models.FloatField()
    mf_date = models.DateField()
    exp_date = models.DateField()

    class Meta:
        db_table = 'drugs'
        verbose_name_plural = 'drugs'

    def __str__(self):
        return self.name