# Generated by Django 4.0.4 on 2022-05-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='username',
            field=models.CharField(max_length=64, verbose_name='사용자명'),
        ),
    ]
