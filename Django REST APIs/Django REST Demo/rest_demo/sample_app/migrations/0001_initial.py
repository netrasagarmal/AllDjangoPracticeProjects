# Generated by Django 4.0.1 on 2022-01-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('sId', models.AutoField(primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=100)),
                ('studentClass', models.IntegerField()),
            ],
        ),
    ]