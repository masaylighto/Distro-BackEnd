# Generated by Django 4.0.3 on 2022-04-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='lang',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.TextField(),
        ),
    ]
