# Generated by Django 4.2.5 on 2023-09-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_userprofile_number_of_answered_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='scores',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
