# Generated by Django 5.1.3 on 2024-11-28 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Category",
                "verbose_name_plural": "Category_list",
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
                verbose_name="Category",
            ),
        ),
    ]
