from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=60)
    pub_date = models.DateField()
    body_text = models.TextField()
    blog_img = models.ImageField(upload_to='images/')
