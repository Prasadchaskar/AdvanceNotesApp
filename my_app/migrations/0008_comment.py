# Generated by Django 3.1.4 on 2020-12-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
