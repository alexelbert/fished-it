from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

STATUS = ((0, "Private"), (1, "Public"))

class Catch(models.Model):
    """
    Stores a single blog catch entry related to :model:`auth.User`.

    Attributes:
        fish_species (CharField): The species of the caught fish.
        fish_length (FloatField): The length of the caught fish.
        fish_weight (FloatField): The weight of the caught fish.
        author (ForeignKey to User): The user who caught the fish.
        featured_image (CloudinaryField): The image of the caught fish.
        created_on (DateTimeField): The timestamp when the catch entry was created.
        updated_on (DateTimeField): The timestamp when the catch entry was last updated.
        public (IntegerField): Indicates whether the catch entry is private or public.
    """
    objects = models.Manager()
    fish_species = models.CharField()
    fish_length = models.FloatField()
    fish_weight = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="catch_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    public = models.IntegerField(choices=STATUS, default=0)
    slug = AutoSlugField(populate_from='fish_species', unique=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.fish_species} caught by {self.author}"



class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`catches.Catch`.

    Attributes:
        post (ForeignKey to Catch): The catch to which the comment belongs.
        author (ForeignKey to User): The user who wrote the comment.
        body (TextField): The content of the comment.
        created_on (DateTimeField): The timestamp when the comment was created.
        approved (BooleanField): Indicates whether the comment is approved or not.
    """
    post = models.ForeignKey(Catch, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
