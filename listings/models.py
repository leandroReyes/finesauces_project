from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering =('-name',)
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('sku',)
        
    def __str__(self):
        return self.name
    