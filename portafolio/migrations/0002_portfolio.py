# Generated by Django 4.2.11 on 2024-05-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('career', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
