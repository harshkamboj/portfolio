from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=250)
    Publish_Date = models.DateTimeField()
    Image = models.ImageField(upload_to='Images/')
    Body = models.TextField()

    def summary(self):
        return  self.Body[:50]

    def pub_date(self):
        return  self.Publish_Date.strftime('%b %e, %Y')

    def __str__(self):
        return self.Title
