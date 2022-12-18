from django.db import models

# Create your models here.

class Mblock(models.Model):
    BLOCK_TYPES = (
        ('def', 'Definition'),
        ('res', 'Result'),
        ('prb', 'Problem'),
    )
    title = models.CharField(max_length=355)
    slug = models.SlugField() # internet adress 
    preview_text = models.TextField() # text that is a summary
    body = models.TextField() # 
    created_at = models.DateTimeField(auto_now_add=True) #automatically filled in when added to DB
    type = models.CharField(max_length=3, choices=BLOCK_TYPES) # type of block



    def get_title(self):
        return self.title

    def get_preview(self):
        return self.previewtext

    class Meta:
        ordering = ("-created_at",)