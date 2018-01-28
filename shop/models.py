from django.db import models


class Detail(models.Model):
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
