# Generated by Django 4.1.1 on 2022-09-28 00:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meta', '0001_initial'),
        ('audio', '0002_rename_country_audioscountry_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagedaudio',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taudios', to='meta.tag'),
        ),
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=29, null=True)),
                ('annotation', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=utils.savePodcastImage, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='podcastsuser', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='podcastslang', to='meta.language')),
            ],
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=29, null=True)),
                ('stars', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('streamed', models.PositiveIntegerField(default=0)),
                ('annotation', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('playlist_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='playlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=29, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('audios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodesaudio', to='audio.audios')),
                ('podcasts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podcastepisodes', to='audio.podcasts')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodetags', to='meta.tag')),
            ],
        ),
        migrations.CreateModel(
            name='AudiosPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('audios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlistaudio', to='audio.audios')),
                ('playlists', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='audiosplaylist', to='audio.playlists')),
            ],
        ),
    ]
