# Generated by Django 5.0.1 on 2024-02-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_hotelcartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelcartitem',
            name='imagecart',
            field=models.ImageField(default='default_image.jpg', upload_to='cart_image'),
        ),
    ]
