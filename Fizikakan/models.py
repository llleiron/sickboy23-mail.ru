from django.db import models
from Grancum.models import Գրանցում
# Create your models here.

class Ֆիզիկական(models.Model):
    հհ = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    Ամսաթիվը = models.DateField(blank=True, null=True, verbose_name='Ամսաթիվը')
    Քաշը = models.IntegerField(blank=True, null=True, verbose_name='Քաշը', help_text='կգ')
    Հասակը = models.IntegerField(blank=True, null=True, verbose_name='Հասակը', help_text='սմ')
    ԿրծքավանդակիՇրջանագիծըՀանգիստ = models.BigIntegerField(help_text='սմ',blank=True, null=True, verbose_name='ԿրծքավանդակիՇրջանագիծըՀանգիստ')
    ԿրծքավանդակիՇրջանագիծըՇնչելիս = models.BigIntegerField(blank=True,help_text='սմ', null=True, verbose_name='ԿրծքավանդակիՇրջանագիծըՇնչելիս')
    ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս = models.BigIntegerField(blank=True,help_text='սմ', null=True, verbose_name='ԿրծքավանդակիՇրջանագիծըԱրտաշնչելիս')
    ՓորիՇրջագիծը = models.BigIntegerField(blank=True, null=True, verbose_name='ՓորիՇրջագիծը')
    Շնչաչափը = models.BigIntegerField(blank=True, null=True, verbose_name='Շնչաչափը')
    ՁեռքիՈՒժաչափըԱջ = models.BigIntegerField(blank=True, null=True, verbose_name='ՁեռքիՈՒժաչափըԱջ')
    ՁեռքիՈՒժաչափըՁախ = models.BigIntegerField(blank=True, null=True, verbose_name='ՁեռքիՈՒժաչափըՁախ')
    def __str__(self):
        return str(self.հհ)