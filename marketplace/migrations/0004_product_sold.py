# Generated by Django 4.2.6 on 2023-11-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_product_card_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]