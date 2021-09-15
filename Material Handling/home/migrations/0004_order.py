# Generated by Django 3.1.7 on 2021-04-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_shop_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('add1', models.TextField()),
                ('add2', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
