# Generated by Django 4.2.7 on 2023-12-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_app', '0003_supplier_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
