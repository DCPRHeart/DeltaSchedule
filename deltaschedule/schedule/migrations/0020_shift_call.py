# Generated by Django 4.2 on 2023-05-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0019_shift_timeblock_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='call',
            field=models.SlugField(default='N1', max_length=63),
            preserve_default=False,
        ),
    ]