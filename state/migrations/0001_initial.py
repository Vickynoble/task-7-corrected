# Generated by Django 4.0.5 on 2022-06-09 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=500)),
                ('home_address', models.CharField(blank=True, max_length=500)),
                ('postalcode', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_id', models.CharField(blank=True, max_length=500)),
                ('origin', models.CharField(blank=True, max_length=500)),
                ('about', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=500)),
                ('people_id_number', models.CharField(blank=True, max_length=500)),
                ('number_of_patient', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=500)),
                ('product_category', models.CharField(blank=True, max_length=500)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('nickname', models.CharField(blank=True, max_length=500)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.address')),
            ],
        ),
    ]
