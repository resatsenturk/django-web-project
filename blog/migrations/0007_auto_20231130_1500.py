# Generated by Django 3.1.5 on 2023-11-30 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_iletisimmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
