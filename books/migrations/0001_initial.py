# Generated by Django 3.2.12 on 2024-01-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('borrowerName', models.CharField(max_length=50, null=True)),
                ('borrowerNumber', models.CharField(max_length=11, null=True)),
                ('borrow_date', models.CharField(max_length=11, null=True)),
                ('return_date', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]