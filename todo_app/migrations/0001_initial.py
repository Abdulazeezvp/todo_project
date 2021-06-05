# Generated by Django 3.2 on 2021-04-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('priority', models.IntegerField(max_length=4)),
            ],
        ),
    ]
