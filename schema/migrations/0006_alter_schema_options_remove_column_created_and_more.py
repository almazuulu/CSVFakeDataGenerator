# Generated by Django 4.0.4 on 2022-05-21 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0005_alter_schema_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schema',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='column',
            name='created',
        ),
        migrations.RemoveField(
            model_name='column',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='schema',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schema',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]