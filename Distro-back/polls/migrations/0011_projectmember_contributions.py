# Generated by Django 4.0.3 on 2022-04-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_projectmember_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmember',
            name='contributions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
