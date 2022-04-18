# Generated by Django 3.2 on 2022-04-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0002_auto_20220418_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='image',
        ),
        migrations.RemoveField(
            model_name='music',
            name='image_url',
        ),
        migrations.AddField(
            model_name='music',
            name='iframe',
            field=models.TextField(default='iframe', max_length=5000),
        ),
    ]
