# Generated by Django 2.0.12 on 2020-04-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grancum', '0003_գրանցում_գրանցմանամսաթիվ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='գրանցում',
            name='ԳրանցմանԱմսաթիվ',
            field=models.DateField(auto_now=True, null=True, verbose_name='Գրանցման ամսաթիվ'),
        ),
    ]
