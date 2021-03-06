# Generated by Django 3.0.7 on 2021-01-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBirthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('birthday', models.DateField(verbose_name='Birthday')),
            ],
        ),
    ]
