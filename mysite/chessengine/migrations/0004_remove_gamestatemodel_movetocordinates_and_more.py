# Generated by Django 4.1.4 on 2022-12-29 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chessengine', '0003_gamestatemodel_totalmoves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamestatemodel',
            name='moveToCordinates',
        ),
        migrations.RemoveField(
            model_name='gamestatemodel',
            name='selectedPieceCordinates',
        ),
        migrations.AddField(
            model_name='chessboardmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='ChessBoardMove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedPiece', models.JSONField()),
                ('moveLocation', models.JSONField()),
                ('result', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('gameState', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chessengine.gamestatemodel')),
            ],
        ),
    ]