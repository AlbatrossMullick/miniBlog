# Generated by Django 5.0.6 on 2024-06-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogger_blogger_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='blogger_photo',
            field=models.ImageField(blank=True, help_text='Profile Picture', null=True, upload_to='images/'),
        ),
    ]
