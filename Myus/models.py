from django.db import models
from Grancum.models import Գրանցում

# Create your models here.
class ՄյուսՄասնագետներ(models.Model):
    հհ = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    Ամսաթիվը = models.DateField(verbose_name='Ամսաթիվը')
    ՀետազոտմանՏվյալներ = models.TextField(verbose_name='ՀետազոտմանՏվյալներ', max_length=1000)
    def __str__(self):
        return str(self.հհ)
