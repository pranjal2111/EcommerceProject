# Generated by Django 5.2 on 2025-04-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_productimage_pimage_productimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='pimage',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
