# Generated by Django 4.2.3 on 2023-10-18 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='content',
        ),
    ]
