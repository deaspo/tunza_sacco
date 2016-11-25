from __future__ import unicode_literals

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
import StringIO

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(max_length=3000)
    pic = models.ImageField(upload_to='products/images')

    # compressing and resizing the image before saving
    def save(self, *args, **kwargs):
        if self.pic:
            img = Img.open(StringIO.StringIO(self.pic.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((1200 * self.pic.width / 1.5, 800 * self.pic.height / 1.5), Img.ANTIALIAS)
            output = StringIO.StringIO()
            img.save(output, format='JPEG', quality=80)
            output.seek(0)

            self.pic = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.pic.name.split('.')[0],
                                              'image/jpeg', output.len, None)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return 'Product: %s' % self.name
