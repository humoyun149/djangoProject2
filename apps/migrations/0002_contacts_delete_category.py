# Generated by Django 5.0.3 on 2024-04-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('addrees', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('numbers', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]