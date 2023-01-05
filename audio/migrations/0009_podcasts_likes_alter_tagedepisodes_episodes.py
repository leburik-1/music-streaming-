# Generated by Django 4.1.1 on 2022-09-29 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0008_episodes_likes_episodes_streamed'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcasts',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tagedepisodes',
            name='episodes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodestag', to='audio.episodes'),
        ),
    ]
