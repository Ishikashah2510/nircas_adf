# Generated by Django 3.2.7 on 2021-10-25 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0005_alter_fooditems_name'),
        ('access', '0002_users_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=255)),
                ('by', models.ForeignKey(limit_choices_to={'user_type': 'Customer'}, on_delete=django.db.models.deletion.DO_NOTHING, to='access.users')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.FloatField(default=0)),
                ('last_date_of_add', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(limit_choices_to={'user_type': 'Customer'}, on_delete=django.db.models.deletion.CASCADE, to='access.users')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.fooditems')),
                ('offer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.everydayoffers')),
                ('user_id', models.ForeignKey(limit_choices_to={'user_type': 'Customer'}, on_delete=django.db.models.deletion.CASCADE, to='access.users')),
            ],
        ),
    ]
