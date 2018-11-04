# Generated by Django 2.1 on 2018-11-04 14:27

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Slug')),
                ('hint', models.CharField(max_length=100, verbose_name='Hint')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Name')),
                ('url', models.CharField(max_length=200, verbose_name='Link')),
                ('target', models.CharField(blank=True, choices=[('_blank', '_blank'), ('_top', '_top'), ('_parent', '_parent')], max_length=10, null=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='Sort')),
                ('active', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menu', to='menu.Menu', verbose_name='Menu type')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.MenuItems')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
    ]
