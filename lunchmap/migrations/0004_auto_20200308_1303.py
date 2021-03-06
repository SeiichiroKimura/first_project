# Generated by Django 3.0.2 on 2020-03-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchmap', '0003_auto_20200308_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
