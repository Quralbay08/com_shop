from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(
        max_length=250,
        verbose_name='category_name:'
    )
    category_slug = models.SlugField(
        max_length=250,
        verbose_name='slug:'
    )
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self):
        return self.category_name

class Brend(models.Model):
    brend_name = models.CharField(
        max_length=250,
        verbose_name='janr_name:'
    )
    brend_slug = models.SlugField(
        max_length=250,
        verbose_name='slug:'
    )
    
    class Meta:
        verbose_name='Brend'
        verbose_name_plural='Brends'
    
    def __str__(self):
        return self.brend_name


class Comments(models.Model):
    text = models.TextField(verbose_name='Text:')  # Vergul ortiqcha edi
    username = models.ForeignKey(User, on_delete=models.CASCADE)  # User modeli bilan bog'langan
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)  # Brend modeli bilan bog'langan
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Comments Date:') 

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment by {self.username} on {self.brend}"


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE)
    
    name = models.CharField(verbose_name='ati:',max_length=255)
    price = models.IntegerField(verbose_name='senasi:')
    image1 = models.ImageField(verbose_name='suwret_1:')
    image2 = models.ImageField(verbose_name='suwret_2:')
    image3 = models.ImageField(verbose_name='suwret_3:')
    sani = models.IntegerField(verbose_name='sani:')
    discriptions = models.TextField(verbose_name='discriptions:')
    
    model_protsessor = models.CharField(verbose_name='Model protsessor:',max_length=50,blank=True,null=True)
    operativnaya_pamyat = models.IntegerField(verbose_name='Operativnaya pamyat (gb):',blank=True,null=True)
    disk_xotirasi = models.IntegerField(verbose_name='Disk xotirasi (gb):',blank=True,null=True)
    display_olchami = models.IntegerField(verbose_name="Displey o'lchami:",blank=True,null=True)
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
    
    def __str__(self):
        return self.name
    