# Generated by Django 3.2.8 on 2021-11-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
