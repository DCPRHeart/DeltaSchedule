# Generated by Django 4.2 on 2023-05-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_alter_shift_linked_alter_shift_work_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='call',
            field=models.CharField(max_length=63, unique=True),
        ),
    ]