# Generated by Django 5.0.1 on 2024-03-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_item_description_delete_itemcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_area',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
