# Generated by Django 4.1.dev20220504101500 on 2022-05-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/%y'),
        ),
    ]
