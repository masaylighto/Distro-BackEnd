# Generated by Django 4.0.3 on 2022-04-16 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_website_link_language_alter_website_link_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contributors',
            new_name='Contributor',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='ProjectMembers',
            new_name='ProjectMember',
        ),
        migrations.RenameModel(
            old_name='Translations',
            new_name='Translation',
        ),
    ]