# Generated by Django 2.2.2 on 2020-08-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricalOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phonenumber', models.CharField(max_length=122)),
                ('product', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phonenumber', models.CharField(max_length=122)),
                ('product', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='ClothingOrder',
        ),
    ]
