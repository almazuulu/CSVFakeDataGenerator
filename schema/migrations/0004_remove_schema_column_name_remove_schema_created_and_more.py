# Generated by Django 4.0.4 on 2022-05-20 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_alter_schema_column_separator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schema',
            name='column_name',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='created',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='order',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='type_column',
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(blank=True, max_length=200, null=True)),
                ('type_column', models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Email', 'Email'), ('Domain name', 'Domain name'), ('Phone number', 'Phone number'), ('Company name', 'Company name'), ('Text', 'Text'), ('Integer', 'Integer'), ('Address', 'Address'), ('Date', 'Date')], max_length=200, null=True)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('schema_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.schema')),
            ],
        ),
    ]
