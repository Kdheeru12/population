# Generated by Django 3.2 on 2021-07-14 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city'),
        ),
    ]