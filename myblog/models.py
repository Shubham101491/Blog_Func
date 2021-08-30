from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now(),null=True)
    published_date = models.DateTimeField(blank=True,null=True)

    # Don't need to be mention everything here
    # but learn new thing

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    # means comment person and blog person are not same
    posted_by = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comment = models.BooleanField(default=False)
    # approved_comment are linked with the func of approved comments

    def __str__(self):
        return self.posted_by