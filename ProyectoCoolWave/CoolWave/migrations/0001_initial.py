# Generated by Django 3.1.2 on 2020-10-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderIndex',
            fields=[
                ('ident', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='car')),
            ],
        ),
    ]