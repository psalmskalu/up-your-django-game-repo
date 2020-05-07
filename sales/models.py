from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from customers.models import Customer
from drugs.models import Drug

# Create your models here.

class Sale(models.Model):
    drug = models.ForegnKey(Drug, on_delete=models.CASCADE)
    #category =    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()
    created_on = models.DateField()
    
    class Meta:
        db_table = 'sales'
        verbose_name_plural = 'sales'

    def __str__(self):
        return self.drug

    def set_user(self, user):
        self.user = user

    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        super(Sale, self).save(*args, **kwargs)
