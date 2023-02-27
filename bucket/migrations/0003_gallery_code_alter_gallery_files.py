# Generated by Django 4.1.7 on 2023-02-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_gallery_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='code',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='files',
            field=models.FileField(null=True, upload_to='media/fb'),
        ),
    ]