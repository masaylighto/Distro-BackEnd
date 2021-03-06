# Generated by Django 4.0.3 on 2022-04-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_rename_contributions_projectmember_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(default='')),
                ('language', models.CharField(default='English', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContributionGuideLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guideLine', models.TextField(default='')),
                ('language', models.CharField(default='English', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contributor',
            name='language',
            field=models.CharField(default='English', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='lang',
            field=models.CharField(default='English', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='language',
            field=models.CharField(default='English', max_length=50),
        ),
    ]
