# Generated by Django 4.1.4 on 2023-01-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chessengine', '0005_chessboardmodel_playerturn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessboardmodel',
            name='playerTurn',
            field=models.CharField(max_length=15),
        ),
    ]