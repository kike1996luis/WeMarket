# Generated by Django 2.1.4 on 2019-07-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0007_auto_20190702_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='photo',
            new_name='photo_f',
        ),
    ]
