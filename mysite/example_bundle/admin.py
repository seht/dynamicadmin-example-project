from dynamicadmin.admin import BundleAdmin, DynamicModelAdmin, register_bundle_model, register_dynamic_models

from .models import ExampleDynamicEntity, ExampleBundle

register_bundle_model(ExampleBundle, model_admin=BundleAdmin)
register_dynamic_models(ExampleBundle, 'example_dynamic_models', model_admin=DynamicModelAdmin,
                        base=ExampleDynamicEntity)
