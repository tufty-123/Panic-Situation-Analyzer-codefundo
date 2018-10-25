# Generated by Django 2.1.2 on 2018-10-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0010_auto_20181022_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisasterArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
                ('lng', models.DecimalField(decimal_places=10, default=0, max_digits=15)),
            ],
        ),
    ]