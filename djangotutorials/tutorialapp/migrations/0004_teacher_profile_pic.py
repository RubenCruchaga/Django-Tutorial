# Generated by Django 4.2.11 on 2024-05-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialapp', '0003_student_profile_pic_alter_student_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
