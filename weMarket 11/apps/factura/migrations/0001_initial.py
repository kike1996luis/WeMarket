# Generated by Django 2.1.4 on 2019-05-27 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('total', models.FloatField(default=0)),
                ('Entregado', models.BooleanField(default=False)),
                ('id_codigo_retiro', models.IntegerField(blank=True, null=True)),
                ('qr', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(blank=True, default=0, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio_venta', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('id_articulo_fk', models.ForeignKey(db_column='id_articulo_fk', on_delete=django.db.models.deletion.CASCADE, to='article.Articulo')),
                ('id_factura_fk', models.ForeignKey(db_column='id_factura_fk', on_delete=django.db.models.deletion.CASCADE, to='factura.Factura')),
            ],
        ),
    ]
