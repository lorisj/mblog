from django.db import models

# Create your models here.


class Mblock(models.Model):
    BLOCK_TYPES = (
        ('Def', 'Definition'),
        ('Res', 'Result'),
        ('Exp', 'Example'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField() # internet adress 
    preview_text = models.TextField() # text that is a summary
    body = models.TextField() # 
    created_at = models.DateTimeField(auto_now_add=True) #automatically filled in when added to DB
    type = models.CharField(max_length=3, choices=BLOCK_TYPES) # type of block
    referenced_by = models.ManyToManyField("Note", blank=True) #link to all notes that reference this block 

    def __str__(self) -> str:
        return f"{self.type}({self.title}):"

    def get_title(self):
        return self.title

    def get_preview(self):
        return self.previewtext

    class Meta:
        ordering = ("-created_at",)


class Note(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    preview_text = models.TextField() # Text that is a summary
    prerequisites = models.ForeignKey("Note", on_delete=models.PROTECT, blank=True, null=True,) # link to other notes

    def __str__(self):
        return self.title
