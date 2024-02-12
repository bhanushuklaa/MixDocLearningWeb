# Generated by Django 4.0.4 on 2022-05-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MixDoc', '0006_freecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtubevideo', models.CharField(max_length=500)),
                ('videotitle', models.CharField(max_length=100)),
                ('videodiscp', models.CharField(max_length=200)),
                ('videochannel', models.CharField(max_length=30)),
                ('videotime', models.CharField(max_length=20)),
                ('videolink', models.CharField(max_length=500)),
            ],
        ),
    ]