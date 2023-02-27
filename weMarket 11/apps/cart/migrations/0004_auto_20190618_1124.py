# Generated by Django 2.1.4 on 2019-06-18 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_clasificacion_descripcion'),
        ('cart', '0003_auto_20190618_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='id_productos_fk',
            field=models.ManyToManyField(to='article.Articulo'),
        ),
        migrations.AddField(
            model_name='carro',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carro',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True),
        ),
    ]
