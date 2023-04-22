# Generated by Django 4.0.6 on 2022-09-08 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='data_ultima_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='produtos/%Y/%m/%d'),
        ),
    ]
