# Generated by Django 4.1.5 on 2023-03-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1033_alter_documenttype_options_alter_tag_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savedviewfilterrule",
            name="rule_type",
            field=models.PositiveIntegerField(
                choices=[
                    (0, "title contains"),
                    (1, "content contains"),
                    (2, "ASN is"),
                    (3, "correspondent is"),
                    (4, "document type is"),
                    (5, "is in inbox"),
                    (6, "has tag"),
                    (7, "has any tag"),
                    (8, "created before"),
                    (9, "created after"),
                    (10, "created year is"),
                    (11, "created month is"),
                    (12, "created day is"),
                    (13, "added before"),
                    (14, "added after"),
                    (15, "modified before"),
                    (16, "modified after"),
                    (17, "does not have tag"),
                    (18, "does not have ASN"),
                    (19, "title or content contains"),
                    (20, "fulltext query"),
                    (21, "more like this"),
                    (22, "has tags in"),
                    (23, "ASN greater than"),
                    (24, "ASN less than"),
                    (25, "storage path is"),
                    (26, "has correspondent in"),
                    (27, "does not have correspondent in"),
                    (28, "has document type in"),
                    (29, "does not have document type in"),
                    (30, "has storage path in"),
                    (31, "does not have storage path in"),
                ],
                verbose_name="rule type",
            ),
        ),
    ]
