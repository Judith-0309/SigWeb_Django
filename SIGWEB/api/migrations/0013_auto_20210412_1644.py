# Generated by Django 3.1.7 on 2021-04-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_donnees'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneesRaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('perimeter', models.IntegerField()),
                ('xCentroid', models.IntegerField()),
                ('yCentroid', models.IntegerField()),
                ('majorAxis', models.IntegerField()),
                ('minAxis', models.IntegerField()),
                ('orientation', models.IntegerField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_donneesraster_related', related_query_name='api_donneesrasters', to='api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('longueur', models.IntegerField()),
                ('taille', models.IntegerField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_ligne_related', related_query_name='api_lignes', to='api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_point_related', related_query_name='api_points', to='api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Polygone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('superficie', models.IntegerField()),
                ('taille', models.IntegerField()),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_polygone_related', related_query_name='api_polygones', to='api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Donnees',
        ),
    ]
