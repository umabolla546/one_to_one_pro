# Generated by Django 3.1 on 2021-04-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='abc',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.student'),
        ),
    ]
