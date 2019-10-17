from django.test import TestCase

# Create your tests here.

from dynamicadmin.models import get_bundle_object, get_dynamic_models, get_dynamic_model, get_dynamic_model_objects
from dynamicadmin.models import BundleEntity, CharField
from .models import ExampleBundle


class ContentTest(TestCase):
    def setUp(self):
        from django.core.management import call_command

        bundle_model = ExampleBundle.objects.create(name='test_bundle_1', label="test bundle 1")
        charfield = CharField(bundle=bundle_model, name="test_charfield")
        charfield.save()
        bundle_model.fields.add(charfield)

        bundle_model.create_dynamic_model(app_label='example_dynamic_models', base=BundleEntity)
        call_command('makemigrations', '--no-input')
        call_command('migrate')

        dynamic_model = get_bundle_object(ExampleBundle, 'test_bundle_1').get_dynamic_model('example_dynamic_models')
        dynamic_model.objects.create(label="example dynamic model", test_charfield="example content")

    def test_content(self):
        dynamic_model = get_bundle_object(ExampleBundle, 'test_bundle_1').get_dynamic_model('example_dynamic_models')
        new_content = dynamic_model.objects.get(test_charfield="example content")

        self.assertEqual(new_content.test_charfield, "example content")
