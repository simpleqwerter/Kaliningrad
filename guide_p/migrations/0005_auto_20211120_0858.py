# Generated by Django 2.2 on 2021-11-20 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide_p', '0004_auto_20211120_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stations',
            options={'ordering': ('station',)},
        ),
    ]
