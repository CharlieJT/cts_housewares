# Generated by Django 2.2 on 2020-03-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about_product',
            field=models.TextField(blank=True, null=True),
        ),
    ]
