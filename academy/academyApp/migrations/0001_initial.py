# Generated by Django 3.1.7 on 2021-03-23 12:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('telephone', models.CharField(blank=True, max_length=120, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('academia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='academyApp.academia')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AcademiaReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academyApp.academia')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('academia', 'user')},
            },
        ),
    ]
