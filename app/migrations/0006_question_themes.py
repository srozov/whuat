# Generated by Django 4.2.5 on 2023-09-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_selectedanswer_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='themes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
