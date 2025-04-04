# Generated by Django 5.1.6 on 2025-02-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adddepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=50)),
                ('departmentcode', models.CharField(max_length=50)),
                ('hod', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='addofficestaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(max_length=50)),
                ('staffid', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('currentaddress', models.CharField(max_length=50)),
                ('choosefile', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='addtechsaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('NET_or_JRF', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('currentaddress', models.CharField(max_length=50)),
                ('choosefile', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='adminviewcmplt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewcomplaint', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lofgin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('usertype', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
