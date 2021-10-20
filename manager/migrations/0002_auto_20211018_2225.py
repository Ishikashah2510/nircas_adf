# Generated by Django 3.2.7 on 2021-10-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditems',
            name='category',
            field=models.CharField(choices=[('Punjabi', 'Punjabi'), ('Chinese', 'Chinese'), ('Sandwich', 'Sandwich'), ('Fast food', 'Fast food'), ('South Indian', 'South Indian'), ('Breakfast', 'Breakfast')], default='Punjabi', max_length=100),
        ),
        migrations.AlterField(
            model_name='fooditems',
            name='rating',
            field=models.FloatField(default=5),
        ),
    ]
