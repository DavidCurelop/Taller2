# Generated by Django 5.0.2 on 2024-03-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
