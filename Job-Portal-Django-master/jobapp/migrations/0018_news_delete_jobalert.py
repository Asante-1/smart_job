# Generated by Django 4.0 on 2022-07-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_jobalert'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=1000, null=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('imageurl', models.URLField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='JobAlert',
        ),
    ]
