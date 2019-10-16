# Generated by Django 2.2.6 on 2019-10-16 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicadmin', '0001_initial'),
        ('example_bundle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleTaxonomyDictionary',
            fields=[
                ('taxonomydictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dynamicadmin.TaxonomyDictionary')),
            ],
            options={
                'abstract': False,
            },
            bases=('dynamicadmin.taxonomydictionary',),
        ),
    ]