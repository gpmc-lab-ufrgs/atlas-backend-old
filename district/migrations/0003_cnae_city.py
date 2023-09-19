# Generated by Django 4.0.6 on 2023-09-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0002_district_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnae_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnae', models.CharField(default='cnae', max_length=255)),
                ('descricao', models.CharField(default='descricao', max_length=1000)),
                ('cod_setor', models.CharField(default='cod_setor', max_length=255)),
                ('nome_setor', models.CharField(default='nome_setor', max_length=1000)),
            ],
        ),
    ]
