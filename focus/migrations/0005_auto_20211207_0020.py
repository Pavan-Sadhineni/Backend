# Generated by Django 3.2.9 on 2021-12-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0004_auto_20211206_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technologyclubs',
            name='hisRole',
        ),
        migrations.AddField(
            model_name='technologyclubs',
            name='clubLogo',
            field=models.CharField(default=False, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologyclubs',
            name='theirRole',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]