# Generated by Django 4.1.1 on 2022-09-25 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review', to='movie_app.review'),
        ),
    ]
