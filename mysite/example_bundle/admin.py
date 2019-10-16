from django.contrib import admin
from dynamicadmin.admin import BundleAdmin, TaxonomyDictionaryAdmin, register_bundle_model, register_dynamic_models
from dynamicadmin.models import BundleEntity
from .models import ExampleBundle, ExampleTaxonomyDictionary


class ExampleBundleAdmin(BundleAdmin):
    pass


register_bundle_model(ExampleBundle, model_admin=ExampleBundleAdmin)
register_dynamic_models(ExampleBundle, 'example_content_models', model_admin=admin.ModelAdmin, base=BundleEntity)

admin.site.register(ExampleTaxonomyDictionary, TaxonomyDictionaryAdmin)
