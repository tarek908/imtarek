# Generated by Django 5.1.1 on 2024-11-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_projects_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
