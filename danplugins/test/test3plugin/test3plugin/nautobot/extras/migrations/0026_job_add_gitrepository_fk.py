# Generated by Django 3.1.14 on 2022-03-07 17:28

from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0025_add_advanced_ui_boolean_to_customfield_conputedfield_and_relationship"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="git_repository",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jobs",
                to="extras.GitRepository",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=nautobot.core.fields.AutoSlugField(
                blank=True,
                max_length=320,
                populate_from=["class_path"],
                unique=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="job",
            unique_together={
                ("grouping", "name"),
                ("source", "git_repository", "module_name", "job_class_name"),
            },
        ),
    ]
