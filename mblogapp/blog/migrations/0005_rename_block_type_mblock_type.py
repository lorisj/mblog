# Generated by Django 4.1.4 on 2022-12-18 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_block_mblock_alter_mblock_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mblock", old_name="block_type", new_name="type",
        ),
    ]
