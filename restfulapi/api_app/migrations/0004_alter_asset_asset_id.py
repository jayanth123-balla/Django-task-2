# Generated by Django 3.2 on 2022-11-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_auto_20221106_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(max_length=50),
        ),
    ]
