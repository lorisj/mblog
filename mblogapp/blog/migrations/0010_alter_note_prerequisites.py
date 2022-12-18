# Generated by Django 4.1.4 on 2022-12-18 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_mblock_referenced_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="prerequisites",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="blog.note",
            ),
        ),
    ]