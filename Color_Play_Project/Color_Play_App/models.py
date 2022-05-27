from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Color_Code_Data(models.Model):
    color_code = models.CharField(max_length=100)
    
    def __str__(self):
        if self.color_code:
            return self.color_code
    
    def color_tag(self):
        if self.color_code is not None:
            return mark_safe('<div style="height:30px; width: 40px; background-color: %s"></div>'%(self.color_code))
