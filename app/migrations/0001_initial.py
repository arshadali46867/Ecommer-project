# Generated by Django 4.2.4 on 2024-05-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'urd'), ('LS', 'Lassi'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('ML', 'Milk')], max_length=2)),
                ('product_image', models.ImageField(upload_to='Productimg')),
            ],
        ),
    ]