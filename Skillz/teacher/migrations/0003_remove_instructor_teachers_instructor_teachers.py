# Generated by Django 4.1.dev20220504101500 on 2022-05-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_course_instructor_course_students_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='teachers',
        ),
        migrations.AddField(
            model_name='instructor',
            name='teachers',
            field=models.ManyToManyField(to='teacher.course'),
        ),
    ]