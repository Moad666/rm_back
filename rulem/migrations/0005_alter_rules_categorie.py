# Generated by Django 4.1.7 on 2024-07-05 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rulem', '0004_remove_categorie_rule_rules_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rulem.categorie'),
        ),
    ]
