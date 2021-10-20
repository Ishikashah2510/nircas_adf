# Generated by Django 3.2.7 on 2021-10-19 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20211018_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='EverydayOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField()),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.fooditems')),
            ],
        ),
    ]
