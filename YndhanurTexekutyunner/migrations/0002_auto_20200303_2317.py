# Generated by Django 2.0.12 on 2020-03-03 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YndhanurTexekutyunner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ընդհանուրտեղեկություններ',
            name='հհ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='գրանցում_id', to='Grancum.Գրանցում'),
        ),
    ]
