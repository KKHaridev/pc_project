# Generated by Django 3.2.3 on 2021-06-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_hospitals_district'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitals',
            old_name='bedsavailable',
            new_name='beds_available',
        ),
    ]