# Generated by Django 3.0.2 on 2020-01-04 19:36

from django.db import migrations, models
import optimized_image.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_preview', optimized_image.fields.OptimizedImageField(blank=True, upload_to='', verbose_name='Images')),
                ('image_alt', models.CharField(blank=True, max_length=255, verbose_name='Images Alt')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=120, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=120, null=True, verbose_name='Title')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='Slug')),
                ('sub_title', models.CharField(blank=True, max_length=120, verbose_name='Sub Title')),
                ('sub_title_ru', models.CharField(blank=True, max_length=120, null=True, verbose_name='Sub Title')),
                ('sub_title_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='Sub Title')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('ordering', models.IntegerField(verbose_name='Ordering')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]
