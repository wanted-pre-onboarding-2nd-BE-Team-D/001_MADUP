# Generated by Django 4.0.4 on 2022-04-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_uid_alter_result_date_alter_result_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='conversion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='cv',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='impression',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
