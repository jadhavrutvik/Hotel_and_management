# Generated by Django 4.2.6 on 2023-11-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0006_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]