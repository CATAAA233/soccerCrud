# Generated by Django 4.1.1 on 2022-09-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='playersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=2)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teamsmodel')),
            ],
        ),
    ]
