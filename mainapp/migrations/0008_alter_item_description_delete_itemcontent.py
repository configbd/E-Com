# Generated by Django 5.0.1 on 2024-03-11 15:09

import prose.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_itemcontent_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=prose.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='ItemContent',
        ),
    ]
