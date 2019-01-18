# Generated by Django 2.0.5 on 2018-05-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_url', models.URLField()),
                ('short_url', models.CharField(max_length=20)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
    ]
