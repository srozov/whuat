# Generated by Django 4.2.5 on 2023-09-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_egg_age_egg_dob_alter_egg_health'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_text',
            new_name='answer_text',
        ),
    ]
