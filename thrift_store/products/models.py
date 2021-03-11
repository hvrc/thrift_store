from django.db import models

class Product(models.Model):
    # (pk) id field is added automatically
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=250, blank=False, default='')
    # seller_id
    # price
    # pictures
    # posted_on
    # Feel free to add any more valid fields
