# Generated by Django 4.1.dev20220504101500 on 2022-05-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_lessons_course_created_course_instructor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]
