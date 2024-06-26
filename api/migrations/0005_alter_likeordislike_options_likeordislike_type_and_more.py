# Generated by Django 5.0.6 on 2024-06-19 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_note_options_remove_note_comment_count_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likeordislike',
            options={'verbose_name': 'Like or Dislike', 'verbose_name_plural': 'Likes or Dislikes'},
        ),
        migrations.AddField(
            model_name='likeordislike',
            name='type',
            field=models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], default='type', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='likeordislike',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_dislikes', to='api.note'),
        ),
        migrations.AlterField(
            model_name='likeordislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likeordislike',
            unique_together={('user', 'note')},
        ),
    ]
