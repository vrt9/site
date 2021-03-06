# Generated by Django 3.2.9 on 2022-02-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bdgameday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3time', models.CharField(blank=True, max_length=15, null=True)),
                ('p3teamviz', models.CharField(blank=True, max_length=45, null=True)),
                ('p3teamhome', models.CharField(blank=True, max_length=45, null=True)),
                ('tvizwl', models.CharField(blank=True, max_length=45, null=True)),
                ('thomwl', models.CharField(blank=True, max_length=45, null=True)),
                ('p3status', models.CharField(blank=True, max_length=45, null=True)),
                ('p3listvizit', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listvizit100', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listvizit75', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listvizit50', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listvizit25', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listvizit0', models.CharField(blank=True, max_length=250, null=True)),
                ('p3status2', models.CharField(blank=True, max_length=45, null=True)),
                ('p3listhome', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listhome100', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listhome75', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listhome50', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listhome25', models.CharField(blank=True, max_length=250, null=True)),
                ('p3listhome0', models.CharField(blank=True, max_length=250, null=True)),
                ('p3date', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'bdgameday',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indextable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=4, null=True)),
                ('player', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('pos', models.CharField(blank=True, max_length=4, null=True)),
                ('min', models.CharField(blank=True, max_length=26, null=True)),
                ('fgm_a', models.CharField(blank=True, max_length=16, null=True)),
                ('number_3pm_a', models.CharField(blank=True, db_column='3pm_a', max_length=16, null=True)),
                ('ftm_a', models.CharField(blank=True, max_length=16, null=True)),
                ('fic', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('def_field', models.IntegerField(blank=True, db_column='def', null=True)),
                ('reb', models.IntegerField(blank=True, null=True)),
                ('ast', models.IntegerField(blank=True, null=True)),
                ('pf', models.IntegerField(blank=True, null=True)),
                ('stl', models.IntegerField(blank=True, null=True)),
                ('blk', models.IntegerField(blank=True, null=True)),
                ('too', models.IntegerField(blank=True, null=True)),
                ('pts', models.IntegerField(blank=True, null=True)),
                ('data', models.CharField(blank=True, max_length=26, null=True)),
            ],
            options={
                'db_table': 'indextable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indextable5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=4, null=True)),
                ('player', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('pos', models.CharField(blank=True, max_length=4, null=True)),
                ('min', models.CharField(blank=True, max_length=26, null=True)),
                ('fgm_a', models.CharField(blank=True, max_length=16, null=True)),
                ('number_3pm_a', models.CharField(blank=True, db_column='3pm_a', max_length=16, null=True)),
                ('ftm_a', models.CharField(blank=True, max_length=16, null=True)),
                ('fic', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('def_field', models.IntegerField(blank=True, db_column='def', null=True)),
                ('reb', models.IntegerField(blank=True, null=True)),
                ('ast', models.IntegerField(blank=True, null=True)),
                ('pf', models.IntegerField(blank=True, null=True)),
                ('stl', models.IntegerField(blank=True, null=True)),
                ('blk', models.IntegerField(blank=True, null=True)),
                ('too', models.IntegerField(blank=True, null=True)),
                ('pts', models.IntegerField(blank=True, null=True)),
                ('data', models.CharField(blank=True, max_length=26, null=True)),
            ],
            options={
                'db_table': 'indextable5',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='T4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3time', models.CharField(blank=True, max_length=45, null=True)),
                ('p3status', models.CharField(blank=True, max_length=45, null=True)),
                ('p3listvizit', models.CharField(blank=True, max_length=245, null=True)),
                ('p3listhome25', models.CharField(blank=True, max_length=245, null=True)),
            ],
            options={
                'db_table': 't4',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tablegameday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p3time', models.CharField(blank=True, max_length=25, null=True)),
                ('p3teamviz', models.CharField(blank=True, max_length=25, null=True)),
                ('p3teamhome', models.CharField(blank=True, max_length=25, null=True)),
                ('tvizwl', models.CharField(blank=True, max_length=10, null=True)),
                ('thomwl', models.CharField(blank=True, max_length=10, null=True)),
                ('p3status', models.CharField(blank=True, max_length=30, null=True)),
                ('p3listvizit', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listvizit100', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listvizit75', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listvizit50', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listvizit25', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listvizit0', models.CharField(blank=True, max_length=230, null=True)),
                ('p3status2', models.CharField(blank=True, max_length=30, null=True)),
                ('p3listhome', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listhome100', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listhome75', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listhome50', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listhome25', models.CharField(blank=True, max_length=230, null=True)),
                ('p3listhome0', models.CharField(blank=True, max_length=230, null=True)),
                ('p3date', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'tablegameday',
                'managed': False,
            },
        ),
    ]
