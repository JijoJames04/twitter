# Generated by Django 4.2.7 on 2023-11-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_formpage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='questions',
            field=models.ManyToManyField(blank=True, to='home.question'),
        ),
        migrations.AlterField(
            model_name='response',
            name='current_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.formpage'),
        ),
    ]
