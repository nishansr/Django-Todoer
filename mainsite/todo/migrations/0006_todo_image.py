# Generated by Django 4.2.2 on 2023-06-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(max_length=250, null=True, upload_to='media/'),
        ),
    ]