# Generated by Django 2.2.5 on 2019-10-09 12:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_auto_20191001_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='comment',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='move',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game'),
        ),
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]