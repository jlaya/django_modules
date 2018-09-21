from django.db import models

def content_file_products(instance, filename):
    return 'apis/products/{0}/{1}'.format(instance, filename)

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=100, default='0',
                                   decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default='0', decimal_places=2,
                                blank=True)
    description = models.TextField(max_length=250, blank=True)
    picture = models.ImageField(upload_to=content_file_products, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
