# Generated by Django 3.1.2 on 2020-10-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoolWave', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionVision',
            fields=[
                ('ident', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
            ],
        ),
    ]
