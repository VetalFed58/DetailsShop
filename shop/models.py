from django.db import models
from django_elasticsearch.models import EsIndexable
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)


class Detail(EsIndexable, models.Model):
    car = models.CharField(max_length=100)
    detail = models.TextField()
    description = models.TextField(null=True)
    price = models.CharField(max_length=30)

    def __unicode__(self):
        return self.detail

    def __str__(self):
        return self.detail

class DetailImage(models.Model):
    detail = models.ForeignKey(Detail, related_name='images',
    on_delete=models.CASCADE)
    image = models.ImageField(upload_to='details', null = True, blank = True)
