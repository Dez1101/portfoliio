from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=60)
    pub_date = models.DateTimeField()
    body_text = models.TextField()
    blog_img = models.ImageField(upload_to='images/')
    id = models.AutoField(primary_key=True)

    # display the titles of the blogs when in admin page
    def __str__(self):
        return self.blog_title

    # return the first 100 words of the blog texts
    def summary(self):
        return self.body_text[:100]

    # return only the date and not time and display in the format month day year
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')