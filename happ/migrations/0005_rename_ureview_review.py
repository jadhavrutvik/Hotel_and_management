# Generated by Django 4.2.6 on 2023-11-02 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0004_rename_name_ureview_n'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ureview',
            new_name='review',
        ),
    ]