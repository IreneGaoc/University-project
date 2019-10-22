# Generated by Django 2.1.5 on 2019-03-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeridersocial', '0005_auto_20190314_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base65'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/markdown', max_length=2000),
        ),
    ]