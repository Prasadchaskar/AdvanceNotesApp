# Generated by Django 3.1.4 on 2020-12-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='bittu', max_length=50),
        ),
    ]