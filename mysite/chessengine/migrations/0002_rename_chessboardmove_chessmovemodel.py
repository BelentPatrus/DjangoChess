# Generated by Django 4.1.4 on 2023-04-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chessengine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChessBoardMove',
            new_name='ChessMoveModel',
        ),
    ]
