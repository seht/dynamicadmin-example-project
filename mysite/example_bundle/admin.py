from django.contrib import admin
from dynamicadmin.admin import BundleAdmin, TaxonomyDictionaryAdmin, register_bundle_model, register_content_models
from dynamicadmin.models import BundleEntity, TaxonomyDictionary
from .models import ExampleBundle, ExampleTaxonomyDictionary


class ExampleBundleAdmin(BundleAdmin):
    pass


register_bundle_model(ExampleBundle, model_admin=ExampleBundleAdmin)
register_content_models(ExampleBundle, 'example_content_models', model_admin=admin.ModelAdmin, base=BundleEntity)

admin.site.register(ExampleTaxonomyDictionary, TaxonomyDictionaryAdmin)
