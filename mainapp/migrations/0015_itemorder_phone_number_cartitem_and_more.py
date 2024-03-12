# Generated by Django 5.0.1 on 2024-03-11 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_remove_itemorder_name_itemorder_being_delivered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemorder',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.item')),
            ],
        ),
        migrations.AlterField(
            model_name='itemorder',
            name='ordered_items',
            field=models.ManyToManyField(to='mainapp.cartitem'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
