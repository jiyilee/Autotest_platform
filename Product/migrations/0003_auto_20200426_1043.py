# Generated by Django 2.1.11 on 2020-04-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200426_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='projectId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='result',
            name='testcaseId',
            field=models.IntegerField(),
        ),
    ]
