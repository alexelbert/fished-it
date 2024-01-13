from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Private"), (1, "Public"))

# Create your models here.


class Catch(models.Model):
    """
    Stores a single blog catch entry related to :model:`auth.User`.
    """
    fish_species = models.CharField(max_length=200)
    fish_length = models.FloatField()
    fish_weight = models.FloatField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="catch_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    public = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.fish_species} caught by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`catches.Catch`.
    """
    post = models.ForeignKey(Catch, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
