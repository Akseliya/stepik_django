# Generated by Django 5.1.4 on 2025-01-16 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0004_category_alter_women_is_published_women_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="women.category"
            ),
        ),
    ]
