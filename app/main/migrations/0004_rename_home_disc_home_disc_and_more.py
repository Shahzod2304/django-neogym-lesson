# Generated by Django 4.2 on 2024-01-26 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_remove_why_img_why_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='home_disc',
            new_name='disc',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='home_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='homecontent',
            old_name='home_content_disc',
            new_name='disc',
        ),
        migrations.RenameField(
            model_name='homecontent',
            old_name='home_content_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='why',
            old_name='why_disc',
            new_name='disc',
        ),
        migrations.RenameField(
            model_name='why',
            old_name='why_title',
            new_name='title',
        ),
    ]
