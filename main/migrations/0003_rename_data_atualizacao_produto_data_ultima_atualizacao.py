# Generated by Django 4.0.6 on 2022-09-08 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_categoria_data_criacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='data_atualizacao',
            new_name='data_ultima_atualizacao',
        ),
    ]