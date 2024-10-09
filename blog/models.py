from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.

# category model

class Category(models.Model):
    """
    Stores a category for each blog post
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT, default=1, related_name="blog_category")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

# meta class added to order the blog posts according to when they were created
    class Meta:
        ordering = ["created_on", "author"]

# method added to make the appearance of the posts in admin more readable
    def __str__(self):
        return f"Title:{self.title} | written by: {self.author}"


# Comment model
class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(max_length=200)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

# meta class added to order the comments by date created
    class Meta:
        ordering = ["created_on", "author"]

# method added to make the appearance more readable in admin
    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
