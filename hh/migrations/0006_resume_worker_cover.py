# Generated by Django 3.1.7 on 2021-04-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0005_remove_resume_worker_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='worker_cover',
            field=models.ImageField(default='images/user.png', upload_to='images/'),
        ),
    ]
