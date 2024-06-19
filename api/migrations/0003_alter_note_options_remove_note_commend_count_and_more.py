# Generated by Django 5.0.6 on 2024-06-19 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_command_user_alter_note_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created'], 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.RemoveField(
            model_name='note',
            name='commend_count',
        ),
        migrations.AddField(
            model_name='note',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(verbose_name='Note Content'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='likeordislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]