# Generated by Django 4.2.7 on 2023-12-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_app', '0002_alter_supplier_bin'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='title',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
    ]
