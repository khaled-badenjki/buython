from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

STATUS = (
    ('True', 'True'),
    ('False', 'False')
)


class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name='products')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
