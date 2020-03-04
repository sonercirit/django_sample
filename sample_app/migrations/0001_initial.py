# Generated by Django 3.0.3 on 2020-03-04 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample_app.Vehicle')),
            ],
        ),
    ]