# Generated by Django 2.2.12 on 2020-06-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190327_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
