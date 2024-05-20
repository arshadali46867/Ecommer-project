# Generated by Django 4.2.4 on 2024-05-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=100)),
                ('passwors2', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PN', 'Paneer'), ('GH', 'Ghee'), ('IC', 'Ice-Creams'), ('CR', 'Curd'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
