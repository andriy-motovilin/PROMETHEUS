# Generated by Django 4.2.5 on 2023-10-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_publication_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=120)),
                ('is_followed', models.CharField(max_length=120)),
            ],
        ),
    ]