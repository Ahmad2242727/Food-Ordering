# Generated by Django 5.0.6 on 2024-06-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipes_name', models.CharField(max_length=1000)),
                ('receipes_discription', models.TextField()),
                ('receipes_image', models.ImageField(blank=True, null=True, upload_to='receipes')),
            ],
        ),
    ]
