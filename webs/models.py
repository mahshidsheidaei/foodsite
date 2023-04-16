from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
#name,text,price,time,ceated,image,type_food

class Food(models.Model):
    FOODS=[
        ('iranifood','غذای ایرانی'),
        ('fastfood','فست وفود'),
        ('juices','نوشیدنی'),
    ]
    
    name=models.CharField(_('نام غذا'),max_length=100)
    text=models.CharField(_('توضیحات'),max_length=50)
    price=models.IntegerField(_('قیمت'),default=100000)
    time=models.IntegerField(_('زمان آماده شدن غذا'),default=2)
    created=models.DateTimeField(_('تاریخ انتشار'),auto_now_add=True)
    image=models.ImageField(_('عکس غذا'),upload_to='webs/')
    type=models.CharField(_('نوع غذا'),max_length=50,choices=FOODS,default='fastfood')
    def __str__(self):
        return self.name