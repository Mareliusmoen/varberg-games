# Generated by Django 4.2.6 on 2023-11-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_product_card_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='card_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
