# Generated by Django 2.2.6 on 2019-10-16 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dynamicadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleBundle',
            fields=[
                ('bundle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dynamicadmin.Bundle')),
            ],
            options={
                'abstract': False,
            },
            bases=('dynamicadmin.bundle',),
        ),
    ]