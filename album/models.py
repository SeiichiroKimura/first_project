from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    comment = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.comment
