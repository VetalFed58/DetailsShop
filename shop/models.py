from django.db import models


class Detail(models.Model):
    author = models.ForeignKey('auth.User')
    car = models.CharField(max_length=100)
    type_of_detail = models.CharField(max_length=50)
    detail = models.TextField()
    description = models.TextField()
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.detail
