# Generated by Django 2.2.6 on 2019-12-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField()),
                ('name', models.CharField(default='', max_length=10)),
            ],
        ),
    ]