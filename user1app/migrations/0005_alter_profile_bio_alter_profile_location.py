# Generated by Django 4.2.3 on 2023-10-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user1app', '0004_alter_upload_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
