# Generated by Django 4.2.6 on 2023-11-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0007_alter_addproduct_image_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
