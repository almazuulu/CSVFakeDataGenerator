# Generated by Django 4.0.4 on 2022-05-23 10:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csvfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('file_created', models.DateTimeField(auto_now_add=True)),
                ('filename', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['-file_created'],
            },
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('column_separator', models.CharField(choices=[('Comma(,)', 'Comma(,)'), ('Semicolon(;)', 'Semicolon(;)'), ('Quotes (“)', 'Quotes (“)'), ('Braces ({})', 'Braces ({})')], max_length=20, null=True)),
                ('string_charachter', models.CharField(choices=[('Double-quote(")', 'Double-quote(")'), ("Single-quote(')", "Single-quote(')")], max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('column_name', models.CharField(blank=True, max_length=200, null=True)),
                ('type_column', models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Email', 'Email'), ('Domain name', 'Domain name'), ('Phone number', 'Phone number'), ('Company name', 'Company name'), ('Text', 'Text'), ('Integer', 'Integer'), ('Address', 'Address'), ('Date', 'Date')], max_length=200, null=True)),
                ('order', models.PositiveIntegerField(blank=True, null=True)),
                ('schema_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.schema')),
            ],
        ),
    ]
