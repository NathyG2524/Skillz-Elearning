# Generated by Django 4.1.dev20220504101500 on 2022-05-18 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(blank=True, null=True, upload_to='images/%y')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('lessons', models.ManyToManyField(blank=True, to='teacher.lessons')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.ManyToManyField(blank=True, to='teacher.section'),
        ),
    ]