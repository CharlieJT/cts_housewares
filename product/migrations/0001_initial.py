# Generated by Django 2.2 on 2020-03-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('about_product', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('image', models.ImageField(upload_to='images')),
                ('stock', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
