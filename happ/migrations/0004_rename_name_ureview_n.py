# Generated by Django 4.2.6 on 2023-11-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0003_ureview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ureview',
            old_name='name',
            new_name='n',
        ),
    ]
