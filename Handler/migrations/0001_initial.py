# Generated by Django 4.1.2 on 2023-01-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Full_Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Contact', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
