# Generated by Django 3.0.2 on 2020-03-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchmap', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
