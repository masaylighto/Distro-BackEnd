# Generated by Django 4.0.3 on 2022-04-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_translations_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='website_link',
            name='language',
            field=models.TextField(default=''),
        ),
    ]