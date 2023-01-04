# Generated by Django 4.1.5 on 2023-01-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('difficulty', models.CharField(choices=[('1', 'easy'), ('2', 'medium'), ('3', 'hard')], max_length=10)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
