# Generated by Django 5.0.1 on 2024-03-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_itemorder_ordered_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemorder',
            name='shipping_area',
        ),
        migrations.AddField(
            model_name='itemorder',
            name='shipping_cost',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
