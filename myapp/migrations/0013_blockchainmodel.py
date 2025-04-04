# Generated by Django 5.1.6 on 2025-03-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_adddepartment_departmentstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockchainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.FloatField()),
                ('data', models.JSONField()),
                ('proof', models.IntegerField()),
                ('previous_hash', models.CharField(max_length=64)),
                ('block_hash', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
