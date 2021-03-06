# Generated by Django 3.2.7 on 2021-09-13 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=8)),
                ('fone', models.CharField(max_length=11)),
                ('posicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_funcionarios.posicao')),
            ],
        ),
    ]
