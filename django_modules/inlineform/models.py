from django.db import models
from ..apis.models import Products

class Invoice(models.Model):
    number = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class InvoiceProduct(models.Model):
    relationship = models.ForeignKey(Invoice, on_delete=True)
    name = models.ForeignKey('apis.Products', on_delete=True)
    quantity = models.DecimalField(max_digits=100, default='0',
                                   decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default='0', decimal_places=2,
                                blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name