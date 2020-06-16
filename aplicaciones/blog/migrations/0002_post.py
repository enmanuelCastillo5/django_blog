# Generated by Django 3.0.5 on 2020-06-16 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='PublicadoNo Publicado')),
                ('feccha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
