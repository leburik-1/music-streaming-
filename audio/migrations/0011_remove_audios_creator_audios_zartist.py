# Generated by Django 4.1.1 on 2022-11-27 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0002_artist_likes'),
        ('audio', '0010_remove_audios_artist_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audios',
            name='creator',
        ),
        migrations.AddField(
            model_name='audios',
            name='zartist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='myaudios', to='Artist.artist'),
            preserve_default=False,
        ),
    ]
