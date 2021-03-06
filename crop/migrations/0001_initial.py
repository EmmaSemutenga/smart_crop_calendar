# Generated by Django 3.2.8 on 2021-11-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('agro_ecological_zone', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=20)),
                ('early_sowing_month', models.PositiveBigIntegerField()),
                ('late_sowing_month', models.PositiveBigIntegerField()),
                ('sowing_value', models.CharField(max_length=10)),
                ('sowing_unit', models.CharField(max_length=20)),
                ('growing_period', models.CharField(max_length=20)),
                ('water_needed', models.CharField(blank=True, max_length=10, null=True)),
                ('challenges', models.TextField()),
            ],
        ),
    ]
