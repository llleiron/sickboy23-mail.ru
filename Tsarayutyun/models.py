from django.db import models
from Grancum.models import Գրանցում
# Create your models here.

class Ծառայություն(models.Model):
    հհ = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    Ամսաթիվը = models.DateField(verbose_name='Ամսաթիվը', blank=True, null=True)
    ԾառայութայնԵվԿենցաղայինՊայմանները = models.TextField(max_length=1000, verbose_name='Ծառայության և կենցաղային պայմանները',null=True, blank=True)
    ԱշխատանքիԲնույթը = models.TextField(max_length=1000, verbose_name='Աշխատանքի բնույթը',null=True, blank=True, help_text='շարային, շտաբային, մանկավարժական և այլն')
    ԲնակկենցաղայինՊայմանները = models.TextField(max_length=1000, verbose_name='Բնակենցաղային պայմանների բնութագիրը',null=True, blank=True)
    Սնունդը = models.TextField(max_length=1000, verbose_name='Սնունդը',null=True, blank=True, help_text='կանոնավոր, անկանոն, օրը քանի անգամ, դիետիկ')
    Քունը = models.TextField(max_length=1000, verbose_name='Քնի տևողությունը և բնույթը',null=True, blank=True)
    ՖիզիկականՊատրաստությունը = models.TextField(max_length=1000, verbose_name='Ֆիզիկական պատրաստությունը։ Ինքնուրույն մարզումները',null=True, blank=True, help_text='պարբերաբար, անկանոն')
    Արձակուրդը = models.TextField(max_length=1000, verbose_name='Արձակուրդը',null=True, blank=True, help_text='որտեղ, երբ է անցկացրել, որ հանգստյան տանը, առողջարանում, տուրիստական արշավում և այլն')
    def __str__(self):
        return str(self.հհ)