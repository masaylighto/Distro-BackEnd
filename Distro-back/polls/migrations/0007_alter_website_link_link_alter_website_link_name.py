# Generated by Django 4.0.3 on 2022-04-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_rename_contributors_contributor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_link',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='website_link',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
