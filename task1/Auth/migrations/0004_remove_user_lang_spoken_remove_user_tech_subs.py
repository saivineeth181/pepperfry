# Generated by Django 4.0.2 on 2022-02-26 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_remove_user_is_individual_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lang_spoken',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tech_subs',
        ),
    ]
