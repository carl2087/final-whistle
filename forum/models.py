from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

STATUS = ((0, 'Draft'), (1, 'Published'))


# Model for creating posts
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    team = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(max_length=300)
    feature_image = CloudinaryField('image', default='placeholder')
    post_content = models.TextField()
    up_votes = models.ManyToManyField(User, related_name='forum_up_votes', blank=True)
    down_votes = models.ManyToManyField(User, related_name='forum_down_votes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def num_of_upvotes(self):
        return self.up_votes.count()

    def num_of_downvotes(self):
        return self.down_votes.count()
