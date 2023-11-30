# Generated by Django 4.2.7 on 2023-11-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_suggestion_form_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='category',
            field=models.TextField(choices=[('guide', 'Guide'), ('tool', 'Tool'), ('resource', 'Resource'), ('article', 'Article'), ('video', 'Video'), ('course', 'Course'), ('other', 'Other')], default='other'),
        ),
    ]
