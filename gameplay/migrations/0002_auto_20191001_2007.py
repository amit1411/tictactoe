# Generated by Django 2.2.5 on 2019-10-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='move',
            name='by_first_player',
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='comment',
            field=models.CharField(max_length=300),
        ),
    ]
