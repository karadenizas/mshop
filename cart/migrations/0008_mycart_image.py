# Generated by Django 3.1.7 on 2021-10-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20211003_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
