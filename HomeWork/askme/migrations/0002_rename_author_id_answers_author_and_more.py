# Generated by Django 4.2 on 2023-05-07 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='answers',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='answer_id',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='author_id',
            new_name='author',
        ),
    ]
