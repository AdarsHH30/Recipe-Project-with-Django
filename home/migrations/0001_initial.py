# Generated by Django 5.1.1 on 2024-09-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_dis', models.TextField()),
                ('recipe_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]