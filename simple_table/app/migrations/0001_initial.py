# Generated by Django 3.1.1 on 2020-11-28 17:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=256)),
                ('field2', models.IntegerField(default=1)),
                ('field3', models.CharField(max_length=256)),
                ('field4', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('table_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(choices=[(None, 'N/A'), ('ch1', 'choice1'), ('ch2', 'choice2'), ('ch3', 'choice3'), ('ch4', 'choice4'), ('ch5', 'choice5')], max_length=256)),
                ('field2', models.IntegerField()),
                ('field3', models.CharField(max_length=256)),
                ('field4', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('table_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Model3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=256)),
                ('field2', models.IntegerField(choices=[(None, 'N/A'), (1, 'choice1'), (2, 'choice2'), (3, 'choice3'), (4, 'choice4'), (5, 'choice5')])),
                ('field3', models.CharField(max_length=256)),
                ('field4', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('table_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
