# Generated by Django 4.2.6 on 2023-11-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0005_rename_ureview_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('copassword', models.CharField(max_length=20)),
            ],
        ),
    ]
