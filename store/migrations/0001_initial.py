# Generated by Django 3.2 on 2021-04-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock_count', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, default='')),
                ('sku', models.CharField(max_length=20, unique=True, verbose_name='Stock Keeping Unit')),
            ],
        ),
    ]
