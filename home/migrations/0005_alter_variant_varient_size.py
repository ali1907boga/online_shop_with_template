# Generated by Django 3.2.8 on 2021-11-12 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211112_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='varient_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.size'),
        ),
    ]
