from django.db import models

# Create your models here.

from dynamicadmin.models import Bundle, TaxonomyDictionary


class ExampleTaxonomyDictionary(TaxonomyDictionary):
    pass


class ExampleBundle(Bundle):
    pass
