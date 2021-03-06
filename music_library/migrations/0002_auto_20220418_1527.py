# Generated by Django 3.2 on 2022-04-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name_plural': 'Music'},
        ),
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='music',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
