# Generated by Django 2.2.12 on 2020-05-12 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, height_field='350px', upload_to='static/Images', width_field='450px'),
            preserve_default=False,
        ),
    ]
