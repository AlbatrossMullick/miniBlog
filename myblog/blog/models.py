from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class BlogPost(models.Model):   
    title = models.CharField(max_length=200, help_text="Please write your blog title")
    blogger_name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(help_text="Please write your blog details")
    post_date = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = _("Blog_Post")
        verbose_name_plural = _("Blog_Posts")
        ordering = ["post_date", 'blogger_name']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_Post_detail", kwargs={"pk": self.pk})
    
    @property
    def short_description(self):
        return f"{self.description[:40]}..."
    

class Comment(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Please write the commenter name")
    comment_date = models.DateTimeField(auto_now=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, help_text="Please write blog for which comment is there")
    comment = models.TextField(help_text="Please write your comment")



    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["comment_date", "comment_by"]

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
    
    @property
    def short_comment(self):
        return f"{self.comment[:40]}..."
    


class Blogger(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Name of the blogger")
    blogger_photo = models.ImageField(upload_to="images/", help_text="Profile Picture", blank=True, null=True)
    phone = models.CharField(max_length=10, help_text="Mobile number", blank=True, null=True)
    

    class Meta:
        verbose_name = _("Blogger")
        verbose_name_plural = _("Bloggers")
        ordering = ['name']

    def __str__(self) -> str:
        return super().__str__()

    def get_absolute_url(self):
        return reverse("blogger_detail", kwargs={"pk": self.pk})




