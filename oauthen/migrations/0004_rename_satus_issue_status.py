# Generated by Django 4.2.3 on 2023-07-30 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauthen', '0003_issue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='satus',
            new_name='status',
        ),
    ]
