# Generated by Django 4.2.6 on 2023-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('image', models.ImageField(upload_to='adproduct/')),
                ('price', models.IntegerField()),
                ('details', models.CharField(max_length=50)),
            ],
        ),
    ]