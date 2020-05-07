from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=100)
    #category =
    description = models.IntegerField()
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    
    class Meta:
        db_table = 'expenses'
        verbose_name_plural = 'expenses'

    def __str__(self):
        return self.title

    def set_user(self, user):
        self.user = user

    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        super(Expense, self).save(*args, **kwargs)
