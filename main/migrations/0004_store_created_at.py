# Generated by Django 3.1 on 2020-09-01 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200901_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
