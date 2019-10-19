from django.db import models
from dynamicadmin.models import Bundle


# Create your models here.


class ExampleDynamicEntity(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.label

    label = models.CharField(max_length=255)


class ExampleBundle(Bundle):
    pass
