from django.db import models

# Create your models here.
class Գրանցում(models.Model):
    Ազգանուն = models.CharField(verbose_name='Ազգանուն', max_length=32,null=True, blank=True)
    Անուն = models.CharField(verbose_name='Անուն', max_length=32,null=True, blank=True)
    Հայրանուն = models.CharField(verbose_name='Հայրանուն', max_length=32,null=True, blank=True) 
    ԳրանցմանԱմսաթիվ = models.DateField(verbose_name='Գրանցման ամսաթիվ',null=True, blank=True, auto_now=True)

    def __str__(self):
        return str(self.id)

