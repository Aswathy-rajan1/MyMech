# Generated by Django 4.1.6 on 2023-05-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_book_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_service',
            name='msg',
            field=models.CharField(max_length=50),
        ),
    ]
