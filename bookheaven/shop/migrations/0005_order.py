# Generated by Django 5.2.1 on 2025-05-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.TextField(default='', max_length=5000)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
