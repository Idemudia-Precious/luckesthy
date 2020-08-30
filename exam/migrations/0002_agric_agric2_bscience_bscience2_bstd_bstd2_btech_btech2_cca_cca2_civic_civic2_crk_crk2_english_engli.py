# Generated by Django 3.1 on 2020-08-28 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='agric2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='bscience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='bscience2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='bstd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='bstd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='btech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='btech2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='cca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='cca2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='civic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='civic2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='crk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='crk2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='english',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='english2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='hecons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='hecons2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='it',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='it2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='phe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='phe2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='sstd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='sstd2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='yoruba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('quest', models.CharField(max_length=600)),
                ('a', models.CharField(max_length=64)),
                ('b', models.CharField(max_length=64)),
                ('c', models.CharField(max_length=64)),
                ('d', models.CharField(max_length=64)),
                ('correct', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='yoruba2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('quest', models.CharField(max_length=600)),
            ],
        ),
    ]
