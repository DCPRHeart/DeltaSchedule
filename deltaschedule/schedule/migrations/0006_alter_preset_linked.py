# Generated by Django 4.2 on 2023-04-29 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_alter_preset_intensity_alter_task_preset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preset',
            name='linked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='schedule.preset'),
        ),
    ]