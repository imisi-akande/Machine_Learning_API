# Generated by Django 2.0.2 on 2018-02-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('fakeness', models.IntegerField()),
            ],
        ),
    ]