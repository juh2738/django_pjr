# Generated by Django 4.0.4 on 2022-06-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_alter_fcuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='', max_length=128, verbose_name='사용자이메일'),
        ),
    ]
