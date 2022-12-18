from django.db import models

# Create your models here.

class Block(models.Model):
    title = models.CharField(max_length=355)
    slug = models.SlugField() # internet adress 
    preview_text = models.TextField() # text that is a summary
    body = models.TextField() # 
    created_at = models.DateTimeField(auto_now_add=True) #automatically filled in when added to DB

