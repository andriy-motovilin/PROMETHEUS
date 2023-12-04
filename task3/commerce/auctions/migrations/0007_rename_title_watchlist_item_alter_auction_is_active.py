# Generated by Django 4.2.4 on 2023-09-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_comments_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='title',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='auction',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active status'),
        ),
    ]