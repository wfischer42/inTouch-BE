# Generated by Django 2.1.7 on 2019-02-16 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20190215_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='frequency',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_contacted',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='next_reminder',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='priority',
            field=models.IntegerField(default=3, null=True),
        ),
    ]