# Generated by Django 5.0.1 on 2024-03-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_itemorder_ordered_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorder',
            name='ordered_items',
            field=models.ManyToManyField(to='mainapp.cartitem'),
        ),
    ]
