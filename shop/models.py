from django.db import models


class Detail(models.Model):
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,)
    car = models.CharField(max_length=100)
    detail = models.TextField()
    description = models.TextField()
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.detail
