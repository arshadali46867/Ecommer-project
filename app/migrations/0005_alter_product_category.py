# Generated by Django 4.2.4 on 2024-05-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_customerregistrationmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('LS', 'Lassi'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('CZ', 'Cheese'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
