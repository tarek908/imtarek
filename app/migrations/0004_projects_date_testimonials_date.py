# Generated by Django 5.1.1 on 2024-11-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_testimonials_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
