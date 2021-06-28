from django.db import models

# Create your models here.

class Category(models.Model):
    

    title = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True, allow_unicode=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(
        Category,  related_name="categoryProduct", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'