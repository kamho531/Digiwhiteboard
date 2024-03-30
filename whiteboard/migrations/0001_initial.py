# Generated by Django 4.2.5 on 2024-03-08 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=30, verbose_name='Last Name')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('hsnnum', models.CharField(max_length=15, verbose_name='HSN')),
                ('ruhnum', models.CharField(max_length=15, verbose_name='RUH Number')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(max_length=15, verbose_name='Gender')),
                ('location', models.CharField(max_length=15, verbose_name='Location')),
                ('status', models.CharField(max_length=15, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=30, verbose_name='Procedure Name')),
                ('diagnosis', models.CharField(max_length=50, verbose_name='Diagnosis')),
                ('comments', models.CharField(max_length=120, verbose_name='Comments')),
                ('admissiondate', models.DateField(verbose_name='Admission Date')),
                ('xray', models.CharField(max_length=15)),
                ('site', models.CharField(max_length=15)),
                ('surgerydate', models.DateField(verbose_name='Surgery Date')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whiteboard.doctors')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='whiteboard.patients')),
            ],
        ),
    ]