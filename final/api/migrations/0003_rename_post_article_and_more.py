# Generated by Django 5.2.3 on 2025-07-13 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_image_alter_post_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
        migrations.RenameModel(
            old_name='PostUserLikes',
            new_name='ArticleUserLikes',
        ),
    ]
